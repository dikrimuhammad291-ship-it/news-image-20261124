#!/usr/bin/env python3
"""Entrypoint for news-image-20261124.

Copies the pre-rendered front page (entry.png, built by render.py) into
the output directory. Standard library only; a byte-for-byte copy, so two
runs always write identical bytes.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(here, "entry.png"),
                    os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
