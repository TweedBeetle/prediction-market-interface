# Kalshi MCP Server - Setup Guide

Quick start guide for setting up the Kalshi MCP server in both demo and production environments.

## Prerequisites

- Python 3.11+
- `uv` package manager installed
- Kalshi account(s) with API access

## Quick Setup

### 1. Install Dependencies

```bash
# From project root
uv sync
```

### 2. Set Up Credentials

#### Create Secrets Directory

```bash
mkdir -p secrets
chmod 700 secrets
```

#### Get Kalshi API Keys

**For Demo Environment:**
1. Sign up at https://demo.kalshi.co
2. Navigate to Settings → API
3. Generate API key pair
4. Save private key:
   ```bash
   # Copy your private key content
   nano secrets/kalshi_demo_private_key.txt
   # Paste content, save (Ctrl+X, Y, Enter)
   chmod 600 secrets/kalshi_demo_private_key.txt
   ```

**For Production Environment:**
1. Sign up at https://kalshi.com
2. Navigate to Settings → API
3. Generate API key pair
4. Save private key:
   ```bash
   nano secrets/kalshi_prod_private_key.txt
   # Paste content, save
   chmod 600 secrets/kalshi_prod_private_key.txt
   ```

### 3. Configure Environment Files

#### Demo Environment

```bash
# Create demo config
cat > .env.kalshi.demo << 'EOF'
KALSHI_API_KEY=your_demo_api_key_here
KALSHI_PRIVATE_KEY_PATH=./secrets/kalshi_demo_private_key.txt
KALSHI_ENVIRONMENT=demo
KALSHI_BASE_URL=https://demo-api.kalshi.co
KALSHI_API_VERSION=v2
EOF

# Secure the file
chmod 600 .env.kalshi.demo
```

Replace `your_demo_api_key_here` with your actual demo API key.

#### Production Environment (Optional)

```bash
# Create production config
cat > .env.kalshi.prod << 'EOF'
KALSHI_API_KEY=your_prod_api_key_here
KALSHI_PRIVATE_KEY_PATH=./secrets/kalshi_prod_private_key.txt
KALSHI_ENVIRONMENT=production
KALSHI_BASE_URL=https://trading-api.kalshi.com
KALSHI_API_VERSION=v2
EOF

# Secure the file
chmod 600 .env.kalshi.prod
```

Replace `your_prod_api_key_here` with your actual production API key.

### 4. Test Server Locally

```bash
# Test demo server (safe - fake money)
uv run run_kalshi_mcp_demo.py

# In another terminal, test a simple call
# (Ctrl+C to stop the server when done)
```

### 5. Register with Claude Code

#### Demo Server (Recommended for testing)

```bash
claude mcp add kalshi_demo --scope project -- bash -c "cd $(pwd) && uv run run_kalshi_mcp_demo.py"
```

#### Production Server (Real money - be careful!)

```bash
claude mcp add kalshi_prod --scope project -- bash -c "cd $(pwd) && uv run run_kalshi_mcp_prod.py"
```

### 6. Enable Project MCP Servers

```bash
# Create or update .claude/settings.json
mkdir -p .claude
cat > .claude/settings.json << 'EOF'
{
  "enableAllProjectMcpServers": true
}
EOF
```

## Verify Setup

### Check Files

```bash
# Verify structure
tree -a -I '__pycache__|*.pyc|.git' -L 2

# Should see:
# ├── .env.kalshi.demo        ✓ (gitignored)
# ├── .env.kalshi.prod        ✓ (gitignored, optional)
# ├── secrets/
# │   ├── kalshi_demo_private_key.txt  ✓
# │   └── kalshi_prod_private_key.txt  ✓ (optional)
# ├── run_kalshi_mcp_demo.py
# ├── run_kalshi_mcp_prod.py
# └── src/kalshi/
```

### Test with Claude Code

```
User: "@kalshi_demo check the exchange status"
Expected: Agent reports if exchange is online

User: "@kalshi_demo what's my balance?"
Expected: Agent returns your demo account balance

User: "@kalshi_demo search for bitcoin markets"
Expected: Agent finds and lists Bitcoin-related markets
```

## Available Tools

For complete list of tools and current implementation status, see **[docs/kalshi-mcp-prd.md](docs/kalshi-mcp-prd.md)**.

## Troubleshooting

### "Invalid API credentials"

- Verify API key is correct in `.env.kalshi.*`
- Check private key file exists and is readable
- Ensure you're using matching environment (demo key → demo API)
- Check for trailing whitespace in credentials

### "Module not found"

- Run `uv sync` to install dependencies
- Use `uv run run_kalshi_mcp_demo.py` (not `python` directly)
- Check you're in project root directory

### "Permission denied" reading private key

```bash
chmod 600 secrets/*
chmod 700 secrets
```

### "Connection failed"

- Check internet connection
- Verify Kalshi API is operational (visit https://kalshi.com)
- For demo: ensure using https://demo-api.kalshi.co
- For prod: ensure using https://trading-api.kalshi.com

### MCP Server Not Showing Up

```bash
# Check MCP servers are registered
claude mcp list

# Verify .claude/settings.json exists and has enableAllProjectMcpServers: true
cat .claude/settings.json

# Check .mcp.json exists (created by claude mcp add)
cat .mcp.json
```

## Security Notes

✅ **Gitignored (never commit):**
- `.env.kalshi.demo`
- `.env.kalshi.prod`
- `secrets/` directory

✅ **Safe to commit:**
- `.env.example`
- `run_kalshi_mcp_*.py`
- Source code in `src/`

## Additional Resources

- **[docs/kalshi-mcp-prd.md](docs/kalshi-mcp-prd.md)** - Current status, features, and roadmap
- **[CLAUDE.md](CLAUDE.md)** - Development patterns and technical reference
- **[Kalshi API Docs](https://docs.kalshi.com)** - Official API documentation
