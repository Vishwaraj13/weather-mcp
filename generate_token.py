#!/usr/bin/env python3
"""
Generate a secure bearer token for MCP server authentication.
"""

import secrets

def generate_token(length: int = 32) -> str:
    """Generate a secure random token."""
    return secrets.token_urlsafe(length)


if __name__ == "__main__":
    token = generate_token()
    print("\n" + "=" * 60)
    print("Generated Secure Bearer Token")
    print("=" * 60)
    print(f"\n{token}\n")
    print("=" * 60)
    print("\nAdd this to your .env file:")
    print(f'MCP_BEARER_TOKEN="{token}"')
    print("=" * 60 + "\n")
