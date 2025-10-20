# GitHub Copilot Configuration

This directory contains configuration files to enhance GitHub Copilot's understanding of the repository.

## Structure

```text
.github/
├── copilot-instructions.md       # Repository-wide instructions
├── instructions/                 # Path-specific instructions
│   ├── src.instructions.md      # Instructions for /src/ directory
│   ├── tests.instructions.md    # Instructions for /tests/ directory
│   └── docs.instructions.md     # Instructions for /docs/ directory
├── prompts/                      # Reusable prompt templates (future)
├── workflows/                    # GitHub Actions workflows
└── pull_request_template.md     # PR template
```

## Purpose

These files help GitHub Copilot Chat understand:
- Project structure and conventions
- Coding standards and best practices
- Testing strategies
- Documentation requirements

## Path-Specific Instructions

The `instructions/` directory contains files named `<directory>.instructions.md` that provide context for specific parts of the repository. When working in a particular directory, Copilot will reference the corresponding instructions file.

## Custom Instructions

The `copilot-instructions.md` file at the repository level provides general project context and conventions that apply across the entire codebase.

## Future Enhancements

The `prompts/` directory is reserved for reusable prompt templates that can be shared across the project for common tasks like:
- Code review prompts
- Testing prompts
- Documentation generation prompts
