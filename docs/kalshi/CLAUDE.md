# Kalshi API Documentation

**Mirror of**: https://docs.kalshi.com/
**Scraped**: 2025-11-03
**Total pages**: 127

## Structure

This documentation mirror preserves the original URL structure as a directory hierarchy for easy navigation.

## Notes

- This is a static mirror - check [docs.kalshi.com](https://docs.kalshi.com/) for the latest updates
- All files preserve original URL in frontmatter for reference
- Base64 images removed for cleaner markdown
- Main content only (navigation/footers stripped by Firecrawl)
- Total mirror size: ~1.5MB of clean markdown

## Regenerating

To update this mirror:
```bash
# 1. Discover URLs
fc-map https://docs.kalshi.com/ > /tmp/kalshi_map.json

# 2. Create mapping (use Python script in /tmp/create_kalshi_mapping.py)
python3 /tmp/create_kalshi_mapping.py

# 3. Scrape
uv run ~/.claude/skills/docs2md/docs2md.py -m /tmp/kalshi_mapping.json -o . -w 10
```
