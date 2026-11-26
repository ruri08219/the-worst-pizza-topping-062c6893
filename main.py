"""The Worst Pizza Topping entry: write the funny line to /output/entry.txt.

Stdlib only. The line is a single sentence, 142 characters.
"""

import os

MAX_CHARS = 200

LINE = "Try our new pizza topped with wet homework \u2014 the cheese holds it together, the crust does the crying, and the dog won't even eat the evidence."


def validate(line):
    """Enforce the gate and the judge's single-line rule."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"line must be 1-{MAX_CHARS} chars, got {len(line)}")
    if line != line.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")


def main():
    validate(LINE)
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
