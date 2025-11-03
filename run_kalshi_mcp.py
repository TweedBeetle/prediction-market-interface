#!/usr/bin/env python3
"""Wrapper script to run the Kalshi MCP server.

This script loads environment variables from .env file before starting the server.
The MCP server validates credentials at module load time, so .env must be loaded first.
"""

from dotenv import load_dotenv

# Load environment variables from .env file (before importing server)
load_dotenv()

if __name__ == "__main__":
    from src.kalshi.kalshi_mcp_server import mcp

    mcp.run()
