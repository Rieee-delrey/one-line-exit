#!/usr/bin/env python3
"""The One-Line Exit: a one-line resignation letter.

Writes the winning line byte-for-byte to /output/entry.txt.
"""

import os

LINE = "Dear Manager, I resign: after three years I have finally been promoted to customer, and customers never answer emails on weekends."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
