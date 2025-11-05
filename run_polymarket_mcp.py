#!/usr/bin/env python3
"""
Wrapper script to run the Polymarket MCP server.

This wrapper ensures environment variables are loaded before
the MCP server initializes.

Usage:
    uv run run_polymarket_mcp.py
"""

from dotenv import load_dotenv

# Load Polymarket environment variables BEFORE importing server
# This ensures credentials are available when clients are initialized
load_dotenv(".env.polymarket", override=True)

if __name__ == "__main__":
    from src.polymarket.polymarket_mcp_server import mcp
    mcp.run()
