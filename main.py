#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes (burn entry).

Writes one original one-line joke about office life to /output/entry.txt.
The judge brief, in order: a genuine one-line office joke, a real turn
at the end, recognition of an office truth, tight wording, and a fresh
take. This line takes the most quoted IT-support script in the office
("have you tried turning it off and on again") and points it at the
one machine nobody can reboot: the speaker's own career.
"""
import os

JOKE = "I asked IT to fix my computer; they asked if I'd tried turning my career off and on again."

OUT = "/output/entry.txt"


def main():
    joke = JOKE.strip()
    assert 1 <= len(joke) <= 199, f"joke must be 1-199 chars, got {len(joke)}"
    assert joke and not joke.isspace(), "joke must not be only whitespace"
    assert "\n" not in joke and "\r" not in joke, "entry must be a single line"
    assert all(ord(c) < 128 for c in joke), "joke must be plain ASCII"
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(joke)
    with open(OUT, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == joke, "read-back mismatch: file differs from joke"
    print(f"wrote {len(joke)} chars to {OUT}")


if __name__ == "__main__":
    main()
