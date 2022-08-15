#!/usr/bin/env python
import subprocess
from pathlib import Path


def create_symlinks(src_dir, target_dir):
    if not target_dir.isdir():
        target_dir.mkdir()

    all_files = list(Path(src_dir).glob("*"))
    for file in all_files:
        target = target_dir / file.name
        if not target.is_symlink():
            target.symlink_to(file)
            print(f"Created symlink for {file}")

def remove_broken_symlinks(target_dir):
    for f in target_dir.glob("*"):
        if f.is_symlink() and not f.exists():
            f.unlink()
            print(f"Removed symlink for {file}")


if __name__ == "__main__":
    src_dir = Path("stylesheets")
    target_dir = Path("../stylelib")

    create_symlinks(src_dir)
    remove_broken_symlinks(target_dir)

