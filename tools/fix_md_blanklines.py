import re
from pathlib import Path


LIST_LINE_RE = re.compile(r"^\s*(?:[-+*]|\d+\.)\s+")


def fix_blanks_around_lists(text: str) -> str:
    lines = text.splitlines()
    out = []
    in_fence = False
    fence_token = None  # ``` or ~~~

    def is_list_line(s: str) -> bool:
        return bool(LIST_LINE_RE.match(s))

    n = len(lines)
    i = 0
    while i < n:
        line = lines[i]

        # Detect fenced code blocks (``` or ~~~)
        stripped = line.lstrip()
        if not in_fence and (stripped.startswith("```") or stripped.startswith("~~~")):
            in_fence = True
            fence_token = stripped[:3]
            out.append(line)
            i += 1
            continue
        if in_fence and fence_token and stripped.startswith(fence_token):
            in_fence = False
            fence_token = None
            out.append(line)
            i += 1
            continue

        if in_fence:
            out.append(line)
            i += 1
            continue

        current_is_list = is_list_line(line)

        # Insert blank line BEFORE the start of a list block
        if current_is_list:
            # Look back to the last line already emitted (previous original line)
            if out:
                prev = out[-1]
                if prev.strip() != "":
                    out.append("")

        out.append(line)

        # Insert blank line AFTER the end of a list block
        if current_is_list:
            # Peek next non-fence context (we're not in a fence here)
            if i + 1 < n:
                nxt = lines[i + 1]
                # If next line is neither blank nor a list line nor end-of-fence start, add a blank line
                nxt_is_list = is_list_line(nxt)
                nxt_is_blank = nxt.strip() == ""
                nxt_starts_fence = nxt.lstrip().startswith("```") or nxt.lstrip().startswith("~~~")
                if not (nxt_is_list or nxt_is_blank or nxt_starts_fence):
                    out.append("")
            else:
                # End of file: do not force extra blank line
                pass

        i += 1

    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def process_repo(root: Path) -> list[tuple[Path, int]]:
    changed = []
    for path in root.rglob("*.md"):
        # Skip node_modules or vendor-like dirs if present
        parts = {p.lower() for p in path.parts}
        if any(x in parts for x in {"node_modules", ".git", "venv", ".venv"}):
            continue

        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            # Try fallback
            original = path.read_text(errors="ignore")

        fixed = fix_blanks_around_lists(original)
        if fixed != original:
            path.write_text(fixed, encoding="utf-8")
            # Count inserted blank lines (approx by diff of line counts when lines added)
            delta = fixed.count("\n") - original.count("\n")
            changed.append((path, delta))

    return changed


if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parents[1]
    changes = process_repo(repo_root)
    for p, d in changes:
        print(f"fixed: {p} (+{d} lines approx)")
    print(f"total files changed: {len(changes)}")

