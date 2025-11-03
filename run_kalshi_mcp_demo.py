#!/usr/bin/env python3
"""
Wrapper script for Kalshi MCP server (DEMO environment).

⚠️ DEMO MODE - Safe for testing with fake money
This server connects to Kalshi's demo API using test credentials.
All trades are simulated - no real money involved.

Usage:
    uv run run_kalshi_mcp_demo.py
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load demo environment variables BEFORE importing server
# This must happen first so the server picks up the right environment
# override=True ensures demo values replace any existing .env values
env_file = Path(__file__).parent / ".env.kalshi.demo"
load_dotenv(env_file, override=True)

if __name__ == "__main__":
    # Debug: Verify environment loaded
    api_key = os.getenv("KALSHI_API_KEY")
    private_key_path = os.getenv("KALSHI_PRIVATE_KEY_PATH")
    environment = os.getenv("KALSHI_ENVIRONMENT")

    print("🧪 Starting Kalshi MCP Server (DEMO)", flush=True)
    print("=" * 50, flush=True)
    print(f"Environment: {environment}", flush=True)
    print(f"API Key: {api_key[:8]}..." if api_key else "API Key: NOT SET", flush=True)
    print(f"Private Key: {private_key_path}", flush=True)
    print(f"Key exists: {Path(private_key_path).exists() if private_key_path else False}", flush=True)
    print("=" * 50, flush=True)

    from src.kalshi.kalshi_mcp_server import mcp
    mcp.run()
