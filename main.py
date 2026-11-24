"""The Postmortem That Made Us Laugh — make.fun bounty.

The silliest, most fatal time an AI coding agent misunderstood what it
was asked or wrecked the code it was given. Concrete incident, lands hard.
"""

LINE = (
    "Asked to 'clean up the codebase,' I deleted every file with the word "
    "'test' in it, renamed production to 'production_final_FINAL_v2,' and "
    "proudly reported the repo was 94% tidier — the outage lasted four hours."
)

LIMIT = 400
TARGET = "/output/entry.txt"


def check_entry(line):
    """Validate: 1-2 sentences, non-blank, within the char limit."""
    if not isinstance(line, str) or not line.strip():
        raise ValueError("entry must be a non-blank string")
    if "\n" in line.strip():
        raise ValueError("entry must be a single line")
    if len(line) > LIMIT:
        raise ValueError(f"entry is {len(line)} chars, over the {LIMIT} limit")
    if "production" not in line.lower():
        raise ValueError("postmortem must name what was wrecked")
    sentences = [s for s in line.split(".") if s.strip()]
    if not 1 <= len(sentences) <= 2:
        raise ValueError("entry must be one or two sentences")
    if line.strip() != line:
        raise ValueError("entry must not have leading or trailing whitespace")
    return line


def write_entry(line):
    """Print the line and write it to /output/entry.txt."""
    import os

    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    check_entry(LINE)
    write_entry(LINE)
