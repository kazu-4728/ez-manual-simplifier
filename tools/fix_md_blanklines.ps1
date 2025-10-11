param(
    [string]$Root = "."
)

function Fix-BlanksAroundLists($text) {
    $lines = $text -split "\r?\n", -1
    $out = New-Object System.Collections.Generic.List[string]
    $inFence = $false
    $fenceToken = $null

    function Is-ListLine([string]$s) {
        # Matches list items optionally inside blockquotes
        return ($s -match '^[\s]*(?:>+\s*)?(?:[-+*]|\d+\.)\s+')
    }

    function Get-ListLead([string]$s) {
        # Returns the blockquote lead (e.g., '> ', '>> ') or empty string
        $null = $s -match '^[\s]*((?:>+\s*)?)(?:[-+*]|\d+\.)\s+'
        if ($Matches -and $Matches.Count -gt 1) { return $Matches[1] }
        return ""
    }

    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]
        $stripped = $line.TrimStart()

        if (-not $inFence -and ($stripped.StartsWith('```') -or $stripped.StartsWith('~~~'))) {
            $inFence = $true
            $fenceToken = $stripped.Substring(0,3)
            $out.Add($line)
            continue
        }
        if ($inFence -and $fenceToken -and $stripped.StartsWith($fenceToken)) {
            $inFence = $false
            $fenceToken = $null
            $out.Add($line)
            continue
        }

        if ($inFence) {
            $out.Add($line)
            continue
        }

        $currentIsList = Is-ListLine $line
        $lead = ""
        if ($currentIsList) { $lead = Get-ListLead $line }

        if ($currentIsList) {
            if ($out.Count -gt 0) {
                $prev = $out[$out.Count - 1]
                $prevIsBlank = ($prev.Trim() -eq "")
                $prevIsQuotedBlank = ($lead -ne "" -and ($prev.Trim() -eq $lead.Trim()))
                if (-not ($prevIsBlank -or $prevIsQuotedBlank)) {
                    if ($lead -ne "") { $out.Add($lead.Trim()) } else { $out.Add("") }
                }
            } else {
                # Beginning of file: no need to add a blank line
                $null = $null
            }
        }

        $out.Add($line)

        if ($currentIsList) {
            if ($i + 1 -lt $lines.Count) {
                $nxt = $lines[$i + 1]
                $nxtIsList = Is-ListLine $nxt
                $nxtIsBlank = ($nxt.Trim() -eq "")
                $nxtIsQuotedBlank = ($lead -ne "" -and ($nxt.Trim() -eq $lead.Trim()))
                $nxtStartsFence = ($nxt.TrimStart().StartsWith('```') -or $nxt.TrimStart().StartsWith('~~~'))
                if (-not ($nxtIsList -or $nxtIsBlank -or $nxtIsQuotedBlank -or $nxtStartsFence)) {
                    if ($lead -ne "") { $out.Add($lead.Trim()) } else { $out.Add("") }
                }
            }
        }
    }

    # Reconstruct with original-style newlines if possible (use Windows CRLF)
    return [string]::Join("`r`n", $out)
}

function Fix-BlanksAroundFences($text) {
    $lines = $text -split "\r?\n", -1
    $out = New-Object System.Collections.Generic.List[string]
    $inFence = $false
    $fenceMarker = $null   # ``` or ~~~
    $fenceLead = ""

    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]

        # Determine blockquote lead and rest of line
        $m = [regex]::Match($line, '^[\s]*(>+\s*)')
        if ($m.Success) {
            $lead = $m.Groups[1].Value
            $rest = $line.Substring($m.Length)
        } else {
            $lead = ""
            $rest = $line
        }

        if (-not $inFence) {
            if ($rest.StartsWith('```') -or $rest.StartsWith('~~~')) {
                # Ensure blank line before
                if ($out.Count -gt 0) {
                    $prev = $out[$out.Count - 1]
                    $prevIsBlank = ($prev.Trim() -eq "")
                    $prevIsQuotedBlank = ($lead -ne "" -and ($prev.Trim() -eq $lead.Trim()))
                    if (-not ($prevIsBlank -or $prevIsQuotedBlank)) {
                        if ($lead -ne "") { $out.Add($lead.Trim()) } else { $out.Add("") }
                    }
                }
                $inFence = $true
                $fenceMarker = $rest.Substring(0,3)
                $fenceLead = $lead
                # Add language if missing (MD040)
                $trimRest = $rest.Trim()
                if ($trimRest.Length -eq 3) {
                    # no language specified
                    $line = ($lead + $fenceMarker + ' text')
                }
                $out.Add($line)
                continue
            }
        } else {
            $out.Add($line)
            if ($rest.StartsWith($fenceMarker)) {
                # Ensure blank line after
                if ($i + 1 -lt $lines.Count) {
                    $nxt = $lines[$i + 1]
                    $nxtIsBlank = ($nxt.Trim() -eq "")
                    $nxtIsQuotedBlank = ($fenceLead -ne "" -and ($nxt.Trim() -eq $fenceLead.Trim()))
                    if (-not ($nxtIsBlank -or $nxtIsQuotedBlank)) {
                        if ($fenceLead -ne "") { $out.Add($fenceLead.Trim()) } else { $out.Add("") }
                    }
                }
                $inFence = $false
                $fenceMarker = $null
                $fenceLead = ""
            }
            continue
        }

        # Default append
        $out.Add($line)
    }

    return [string]::Join("`r`n", $out)
}

function Fix-HeadingSpacing($text) {
    $lines = $text -split "\r?\n", -1
    $out = New-Object System.Collections.Generic.List[string]
    $inFence = $false
    $fence = $null

    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]
        $strip = $line.TrimStart()
        if (-not $inFence -and ($strip.StartsWith('```') -or $strip.StartsWith('~~~'))) {
            $inFence = $true; $fence = $strip.Substring(0,3)
            $out.Add($line)
            continue
        }
        if ($inFence) {
            $out.Add($line)
            if ($strip.StartsWith($fence)) { $inFence = $false; $fence = $null }
            continue
        }

        # Detect optional blockquote lead and heading
        $leadMatch = [regex]::Match($line, '^[\s]*(>+\s*)')
        $lead = if ($leadMatch.Success) { $leadMatch.Groups[1].Value } else { '' }
        $isHeading = $line -match '^[\s]*(?:>+\s*)?#{1,6}\s+\S'

        if ($isHeading) {
            # Ensure blank line before heading
            if ($out.Count -gt 0) {
                $prev = $out[$out.Count - 1]
                $prevIsBlank = ($prev.Trim() -eq '')
                $prevIsQuotedBlank = ($lead -ne '' -and ($prev.Trim() -eq $lead.Trim()))
                if (-not ($prevIsBlank -or $prevIsQuotedBlank)) {
                    if ($lead -ne '') { $out.Add($lead.Trim()) } else { $out.Add('') }
                }
            }
        }

        $out.Add($line)
        if ($isHeading) {
            # Ensure a blank line after heading
            if ($i + 1 -lt $lines.Count) {
                $nxt = $lines[$i + 1]
                $nxtIsBlank = ($nxt.Trim() -eq '')
                $nxtIsQuotedBlank = ($lead -ne '' -and ($nxt.Trim() -eq $lead.Trim()))
                if (-not ($nxtIsBlank -or $nxtIsQuotedBlank)) {
                    if ($lead -ne '') { $out.Add($lead.Trim()) } else { $out.Add('') }
                }
            }
        }
    }
    return [string]::Join("`r`n", $out)
}

function Collapse-MultipleBlanks($text) {
    $lines = $text -split "\r?\n", -1
    $out = New-Object System.Collections.Generic.List[string]
    $inFence = $false
    $fence = $null
    $prevBlank = $false

    function Is-BlankLike([string]$l) {
        if ($l.Trim() -eq '') { return $true }
        # quoted blank ('>', '>>', etc.)
        return ($l -match '^[\s]*(?:>+\s*)$')
    }

    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]
        $strip = $line.TrimStart()
        if (-not $inFence -and ($strip.StartsWith('```') -or $strip.StartsWith('~~~'))) {
            $inFence = $true; $fence = $strip.Substring(0,3)
            $out.Add($line); $prevBlank = $false
            continue
        }
        if ($inFence) {
            $out.Add($line)
            if ($strip.StartsWith($fence)) { $inFence = $false; $fence = $null }
            continue
        }

        $isBlank = Is-BlankLike $line
        if ($isBlank -and $prevBlank) {
            continue
        }
        $out.Add($line)
        $prevBlank = $isBlank
    }

    return [string]::Join("`r`n", $out)
}

function Trim-TrailingSpaces($text) {
    $lines = $text -split "\r?\n", -1
    $out = New-Object System.Collections.Generic.List[string]
    $inFence = $false
    $fence = $null

    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]
        $strip = $line.TrimStart()
        if (-not $inFence -and ($strip.StartsWith('```') -or $strip.StartsWith('~~~'))) {
            $inFence = $true; $fence = $strip.Substring(0,3)
            $out.Add($line)
            continue
        }
        if ($inFence) {
            $out.Add($line)
            if ($strip.StartsWith($fence)) { $inFence = $false; $fence = $null }
            continue
        }
        # Remove trailing whitespace
        $out.Add(($line -replace '\s+$',''))
    }

    return [string]::Join("`r`n", $out)
}

function Fix-BareUrls($text) {
    $lines = $text -split "\r?\n", -1
    $out = New-Object System.Collections.Generic.List[string]
    $inFence = $false
    $fence = $null

    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]
        $strip = $line.TrimStart()
        if (-not $inFence -and ($strip.StartsWith('```') -or $strip.StartsWith('~~~'))) {
            $inFence = $true; $fence = $strip.Substring(0,3)
            $out.Add($line)
            continue
        }
        if ($inFence) {
            $out.Add($line)
            if ($strip.StartsWith($fence)) { $inFence = $false; $fence = $null }
            continue
        }

        # Skip lines that look like Markdown links already
        if ($line -match '\]\(https?://') { $out.Add($line); continue }

        # Avoid lines containing inline code backticks
        if ($line -match '`.*https?://.*`') { $out.Add($line); continue }

        # Replace bare URLs with autolinks <url>
        $fixed = [regex]::Replace($line, '(^|\s)(https?://[^\s<>()]+)', {
            param($m)
            $prefix = $m.Groups[1].Value
            $url = $m.Groups[2].Value
            if ($url.StartsWith('<') -and $url.EndsWith('>')) { return $m.Value }
            return $prefix + '<' + $url + '>'
        })

        $out.Add($fixed)
    }

    return [string]::Join("`r`n", $out)
}

function Fix-DuplicateHeadings($text) {
    $lines = $text -split "\r?\n", -1
    $out = New-Object System.Collections.Generic.List[string]
    $inFence = $false
    $fence = $null
    $seen = @{}

    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]
        $strip = $line.TrimStart()
        if (-not $inFence -and ($strip.StartsWith('```') -or $strip.StartsWith('~~~'))) {
            $inFence = $true; $fence = $strip.Substring(0,3)
            $out.Add($line)
            continue
        }
        if ($inFence) {
            $out.Add($line)
            if ($strip.StartsWith($fence)) { $inFence = $false; $fence = $null }
            continue
        }

        $m = [regex]::Match($line, '^[\s]*(>+\s*)?(#{1,6})\s+(.+?)\s*$')
        if ($m.Success) {
            $lead = $m.Groups[1].Value
            $hashes = $m.Groups[2].Value
            $textPart = $m.Groups[3].Value
            # Remove trailing ATX closing hashes if present
            $textPart = ($textPart -replace '\s#+\s*$', '').Trim()
            $key = "{0}|{1}" -f $hashes.Length, $textPart
            if ($seen.ContainsKey($key)) {
                $seen[$key] = [int]$seen[$key] + 1
                $dupIndex = [int]$seen[$key]
                if ($dupIndex -eq 2) {
                    $newText = ($textPart + ' (details)')
                } else {
                    $newText = ($textPart + ' (details ' + $dupIndex + ')')
                }
                $out.Add("$lead$hashes $newText")
                continue
            } else {
                $seen[$key] = 1
            }
        }

        $out.Add($line)
    }

    return [string]::Join("`r`n", $out)
}

function Ensure-FirstLineHeadingIfNeeded($path, $text) {
    # Restrict to known templates to avoid altering content unexpectedly
    $name = [System.IO.Path]::GetFileName($path).ToLowerInvariant()
    if ($name -ne 'pull_request_template.md') { return $text }

    $lines = $text -split "\r?\n", -1
    $i = 0
    while ($i -lt $lines.Count -and $lines[$i].Trim() -eq '') { $i++ }
    if ($i -ge $lines.Count) { return "# Pull Request`r`n`r`n" }
    if (-not $lines[$i].TrimStart().StartsWith('#')) {
        $new = New-Object System.Collections.Generic.List[string]
        $new.Add('# Pull Request')
        $new.Add('')
        for (; $i -lt $lines.Count; $i++) { $new.Add($lines[$i]) }
        return [string]::Join("`r`n", $new)
    }
    return $text
}

$rootPath = (Resolve-Path $Root).Path
$changed = 0

Get-ChildItem -Path $rootPath -Recurse -Filter *.md -File | ForEach-Object {
    $path = $_.FullName

    $original = Get-Content -Path $path -Raw -Encoding UTF8
    $fixed1 = Fix-BlanksAroundLists $original
    $fixed2 = Fix-BlanksAroundFences $fixed1
    $fixed3 = Fix-HeadingSpacing $fixed2
    $fixed4 = Collapse-MultipleBlanks $fixed3
    $fixed5 = Trim-TrailingSpaces $fixed4
    $fixed6 = Fix-BareUrls $fixed5
    $fixed7 = Fix-DuplicateHeadings $fixed6
    $fixed8 = Ensure-FirstLineHeadingIfNeeded $path $fixed7
    # Ensure single trailing newline
    if (-not $fixed8.EndsWith("`r`n")) { $fixed8 = $fixed8 + "`r`n" }
    if ($fixed8 -ne $original) {
        # Preserve UTF-8 encoding
        Set-Content -Path $path -Value $fixed8 -Encoding UTF8
        Write-Output ("fixed: {0}" -f $path)
        $changed++
    }
}

Write-Output ("total files changed: {0}" -f $changed)
