#!/usr/bin/env python
from pathlib import Path


def create_symlinks(src_dir, target_dir):
    if not target_dir.is_dir():
        target_dir.mkdir()
        print(f"Created directory {target_dir}")

    all_files = list(Path(src_dir).glob("*"))
    for file in all_files:
        target = target_dir / file.name
        if not target.is_symlink():
            src_abs = file.absolute()
            target.symlink_to(src_abs)
            print(f"Created symlink for {file}")

def remove_broken_symlinks(target_dir):
    for f in target_dir.glob("*"):
        if f.is_symlink() and not f.exists():
            f.unlink()
            print(f"Removed symlink for {f}")


if __name__ == "__main__":
    src_dir = Path("stylesheets")
    target_dir = Path("../stylelib")

    create_symlinks(src_dir, target_dir)
    remove_broken_symlinks(target_dir)

