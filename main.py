"""One-sentence absurd invention pitch: emit the fixed sentence.

The entry text is fixed by the bounty brief; this program simply
assembles it from its parts and writes it, byte for byte, to
/output/entry.txt. No input, no randomness, no dependencies.
"""

from pathlib import Path


def build_sentence() -> str:
    """Return the fixed pitch sentence."""
    subject = "A washing machine"
    action = "that holds one sock hostage per load"
    condition = "until you confess where all the others went"
    return f"{subject} {action} {condition}."


def write_entry(path: Path, text: str) -> None:
    """Write the sentence to path, creating parent dirs as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    sentence = build_sentence()
    write_entry(Path("/output/entry.txt"), sentence)


if __name__ == "__main__":
    main()
