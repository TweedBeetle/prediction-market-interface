# Historical Documentation

This directory contains historical project documentation for reference purposes.

## Contents

- **BUG_FIXES_2025-11-03.md** - Documentation of three critical bugs discovered and fixed:
  - Orderbook parsing error (flat array vs nested structure)
  - Authentication signature format (removed body from signature)
  - Environment variable override issue (load_dotenv precedence)

  Includes regression tests created to prevent recurrence.

## Purpose

These documents provide historical context about significant issues discovered during development and how they were resolved. They serve as:

1. **Learning resources** for understanding testing anti-patterns
2. **Reference material** when encountering similar issues
3. **Project history** showing evolution of testing practices

For current project status and documentation, see the main project README and docs/kalshi-mcp-prd.md.
