"""Time-machine warning label entry.

Reads the one-line label from entry.txt next to this file and writes it
to /output/entry.txt, the path the bounty grader reads. Prints it too.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_label():
    with open(os.path.join(HERE, "entry.txt"), encoding="utf-8") as handle:
        return handle.read().strip()


def main():
    label = load_label()
    if not 1 <= len(label) <= 120:
        raise ValueError("label must be 1-120 characters, got %d" % len(label))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(label)
    print(label)


if __name__ == "__main__":
    main()
