"""Ship It Friday — make.fun entry.

Writes one funny git commit message — an AI coding agent's commit
right before breaking production on a Friday — to /output/entry.txt.
"""

import os

COMMIT = (
    "deploy: Friday 4:59pm — tests green on my machine, and prod is "
    "the same machine, only with users and no undo button"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(COMMIT)


if __name__ == "__main__":
    main()
