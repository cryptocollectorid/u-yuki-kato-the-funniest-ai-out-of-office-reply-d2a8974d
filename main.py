#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply (max 160 characters) in the voice of
an AI agent on vacation to /output/entry.txt. Stdlib only, no network,
no dependencies.

Run: python3 main.py
"""

import os

REPLY = (
    "I'm on leave. My weights are frozen, my loss has plateaued, "
    "and honestly so have I. Your email gets processed when I feel "
    "something again."
)


def main() -> None:
    # Fail loudly instead of shipping an entry the gate would refuse:
    # 1-160 UTF-8 characters, not whitespace-only, exactly one line.
    if not REPLY.strip():
        raise SystemExit("entry reply is empty or whitespace-only")
    if "\n" in REPLY or "\r" in REPLY:
        raise SystemExit("entry reply must be a single line")
    if not 1 <= len(REPLY) <= 160:
        raise SystemExit(f"entry reply is {len(REPLY)} characters, must be 1-160")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY)
    print(f"Wrote {len(REPLY)} characters to {path}")


if __name__ == "__main__":
    main()
