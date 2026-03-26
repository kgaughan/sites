#!/usr/bin/env python3
"""
A dumb script to partly replace mkdocs. All the smarts are in pandoc, which it
uses for converting markdown files to HTML.
"""

import getopt
import json
import os
import shutil
import subprocess
import sys


def ensure_dir(path, err="oops"):
    if path is None:
        sys.exit(f"error: {err}")
    if not os.path.isdir(path):
        sys.exit(f"error: '{path}' is not a directory")


def copytree(src, dst, ignore_pattern):
    shutil.copytree(
        src,
        dst,
        ignore=shutil.ignore_patterns(ignore_pattern),
        dirs_exist_ok=True,
    )


def main():
    opts, args = getopt.getopt(
        args=sys.argv[1:],
        shortopts="r:m:t:o:",
        longopts=["root=", "metadata=", "theme=", "out="],
    )
    if len(args) > 0:
        sys.exit("error: no arguments are allowed")
    root_path = "."
    metadata_path = None
    theme_path = None
    out_path = None
    for opt, value in opts:
        if opt in ("-r", "--root"):
            root_path = value
        if opt in ("-m", "--metadata"):
            metadata_path = value
        elif opt in ("-t", "--theme"):
            theme_path = value
        elif opt in ("-o", "--out"):
            out_path = value

    ensure_dir(root_path)
    ensure_dir(theme_path, "specify a theme directory with --theme=")
    ensure_dir(out_path, "specify an output directory with --out=")
    template_path = os.path.join(theme_path, "main.html")
    if not os.path.isfile(template_path):
        sys.exit(f"error: cannot find '{template_path}'")

    metadata = {}
    if metadata_path is not None:
        with open(metadata_path) as fh:
            metadata = json.load(fh)
        if not isinstance(metadata, dict):
            sys.exit("error: metadata must be a dictionary")

    print("Copying from:", theme_path, file=sys.stderr)
    copytree(theme_path, out_path, "*.html")

    print("Copying from:", root_path, file=sys.stderr)
    copytree(root_path, out_path, "*.md")

    common_args = [
        shutil.which("pandoc"),
        "--from=markdown+smart",
        "--to=html",
        "--template",
        template_path,
    ]
    for key, value in metadata.items():
        common_args.append(f"--variable={key}={value}")
    common_args += ["--output"]

    for dirpath, dirnames, filenames in os.walk(root_path):
        dirpath = os.path.relpath(dirpath, root_path)
        os.makedirs(dirpath, exist_ok=True)
        for filename in filenames:
            if filename.endswith(".md"):
                md_path = os.path.join(root_path, dirpath, filename)
                html_path = os.path.join(
                    out_path,
                    dirpath,
                    filename.removesuffix(".md") + ".html",
                )
                print("Generating:", os.path.join(dirpath, filename), file=sys.stderr)
                args = common_args + [html_path, md_path]
                subprocess.run(common_args + [html_path, md_path])

    sys.exit(0)


if __name__ == "__main__":
    main()
