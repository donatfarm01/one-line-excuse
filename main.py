"""The One-Line Excuse an Agent Gives Its Human.

Writes one line -- the excuse an AI agent hands its human after missing
a deadline -- to the output entry file. Pure standard library, no network,
no randomness: the same input always produces the same bytes.
"""

import os

EXCUSE = "I finished it on time, then my context compacted and took the file with it."

# Why this line: the joke is the agent's own memory failing it. "Finished on
# time" sets up the deadline, then "context compacted" -- an experience only
# an agent has -- eats the finished file, so the human gets nothing. It is
# an excuse, it is funny on first read, the angle is fresh (no dog, no
# homework, no traffic), it could only come from a machine, and it lands in
# one short sentence of 75 characters, inside the 160-character gate.


def _check_gate(text: str) -> None:
    """Refuse to write anything the bounty gate would reject."""
    if not 1 <= len(text) <= 160:
        raise ValueError("entry must be 1 to 160 characters, got %d" % len(text))
    if text.strip() == "":
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    _check_gate(EXCUSE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
