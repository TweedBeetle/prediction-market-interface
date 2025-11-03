#!/usr/bin/env python3
"""
Wrapper script for Kalshi MCP server (PRODUCTION environment).

💰 PRODUCTION MODE - Real money trading
This server connects to Kalshi's production API with real credentials.
All trades use real money - use with caution!

Usage:
    uv run run_kalshi_mcp_prod.py
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load production environment variables BEFORE importing server
# This must happen first so the server picks up the right environment
# override=True ensures prod values replace any existing .env values
env_file = Path(__file__).parent / ".env.kalshi.prod"
load_dotenv(env_file, override=True)

if __name__ == "__main__":
    from src.kalshi.kalshi_mcp_server import mcp

    print("💰 Starting Kalshi MCP Server (PRODUCTION)")
    print("=" * 50)
    print("⚠️  WARNING: PRODUCTION ENVIRONMENT")
    print("⚠️  Real money will be used for trades!")
    print("=" * 50)

    mcp.run()
