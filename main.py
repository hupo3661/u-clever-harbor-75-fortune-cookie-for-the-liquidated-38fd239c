#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes the one fortune cookie line for a crypto trader who has just
been liquidated to $MAKEFUN_OUTPUT_DIR/entry.txt (the grader sets it
to /output/entry.txt). One line, 76 characters, 13 words, no trailing
newline so the file holds exactly the message.
"""

import os

LINE = "You will meet a wealthy stranger. He is you, before you discovered leverage."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
