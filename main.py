#!/usr/bin/env python3
"""The One-Line Exit: a one-line resignation letter.

Writes the winning line byte-for-byte to /output/entry.txt, then reads the
file back and verifies the written bytes with a sha256 check.
"""

import hashlib
import os

LINE = "Dear Manager, I resign: after three years I have finally been promoted to customer, and customers never answer emails on weekends."

EXPECTED_SHA256 = "a7a21a6f1742316fbbe2aa43798acb2feb9a404a3178012f4865c16e0368cbae"


def main():
    # Gate: one line, 1-140 chars, no trailing newline.
    assert LINE, "entry must not be empty"
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 140, f"entry is {len(LINE)} chars, gate is 1-140"
    assert LINE == LINE.strip(), "entry must not have leading/trailing whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

    # Read-back verification: the bytes on disk must match the line exactly.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == LINE.encode("utf-8"), "written bytes differ from the line"
    digest = hashlib.sha256(written).hexdigest()
    assert digest == EXPECTED_SHA256, f"sha256 mismatch: {digest}"
    print(f"wrote {len(written)} bytes, sha256 {digest}")


if __name__ == "__main__":
    main()
