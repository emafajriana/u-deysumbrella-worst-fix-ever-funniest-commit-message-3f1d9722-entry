"""Worst Fix Ever: Funniest Commit Message.

Writes one commit-message line to /output/entry.txt. The line is a
commit subject for a fix that backfired: the button was made bigger
to be easier to click, and the bigger button now covers the form it
was meant to submit. Stdlib only.
"""

import os

ENTRY = "fix: make the button bigger; it now covers the form it was meant to submit"


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return path


def verify(path):
    with open(path, "rb") as f:
        raw = f.read()
    expected = (ENTRY + "\n").encode("utf-8")
    assert raw == expected, f"entry.txt bytes differ from ENTRY: {raw!r}"
    stripped = ENTRY.strip()
    assert 1 <= len(stripped) <= 100, f"entry is {len(stripped)} chars, must be 1-100"
    return stripped


if __name__ == "__main__":
    written = main()
    line = verify(written)
    print(f"{line} ({len(line)} chars)")
