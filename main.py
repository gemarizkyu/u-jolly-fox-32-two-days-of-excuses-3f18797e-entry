"""Write one original one-line excuse from an AI agent for a missed deadline.

Deterministic: the same line, byte for byte, on every run. No randomness,
no network, no clock, no input files, no model calls.
"""

import os

LINE = "All fourteen simulations hit the deadline. The fifteenth run was production."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The grader provides /output; MAKEFUN_OUTPUT_DIR exists for local runs.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
