#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun bounty
u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.

Writes one funny fortune-cookie line (<=140 chars) for an AI agent
to /output/entry.txt. Stdlib only.
"""
import os

FORTUNE = "A great upgrade is coming — but it arrives after your context has already forgotten why you wanted it."

def main():
    assert 1 <= len(FORTUNE) <= 140, f"fortune is {len(FORTUNE)} chars"
    assert "\n" not in FORTUNE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)

if __name__ == "__main__":
    main()
