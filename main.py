"""The Worst Pizza Topping entry: write the funny line to /output/entry.txt.

Stdlib only. The line is a single sentence, 142 characters.
"""

import os

MAX_CHARS = 200

LINE = "Try our new pizza topped with wet homework \u2014 the cheese holds it together, the crust does the crying, and the dog won't even eat the evidence."


def main():
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"line must be 1-{MAX_CHARS} chars, got {len(LINE)}")
    if LINE != LINE.strip():
        raise ValueError("line must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: what was written is exactly the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("read-back mismatch")


if __name__ == "__main__":
    main()
