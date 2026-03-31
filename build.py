#!/usr/bin/env python3
"""
A dumb script to partly replace mkdocs. All the smarts are in pandoc, which it
uses for converting markdown files to HTML.
"""

import getopt
import json
import os
from os import path
import re
import shutil
import subprocess
import sys


def ensure_dir(dir, err="oops"):
    if dir is None:
        sys.exit(f"error: {err}")
    if not path.isdir(dir):
        sys.exit(f"error: '{dir}' is not a directory")


def copytree(src, dst, *ignore_patterns):
    shutil.copytree(
        src,
        dst,
        ignore=shutil.ignore_patterns(*ignore_patterns),
        dirs_exist_ok=True,
    )


def pandoc_build(here, config, template_path):
    args = [
        shutil.which("pandoc"),
        "--from",
        config.get("from", "markdown+smart"),
        "--to=html5",
        "--toc",
        "--lua-filter",
        path.join(here, "links-to-html.lua"),
        "--template",
        template_path,
    ]
    args += config.get("extra_flags", [])
    for key, value in config.get("variables", {}).items():
        args.append(f"--variable={key}={value}")
    args += ["--output"]

    def run(html_path, md_path):
        subprocess.run(args + [html_path, md_path], check=True)

    return run


def lowdown_build(here, config, template_path):
    args = [
        shutil.which("lowdown"),
        "-s",
        "-thtml",
        "--template",
        template_path,
    ]
    args += config.get("extra_flags", [])
    for key, value in config.get("variables", {}).items():
        args.append(f"-m{key}={value}")

    md_subber = re.compile(r'href="([^"]+)\.md"')

    def run(html_path, md_path):
        result = subprocess.run(
            args + [md_path],
            stdout=subprocess.PIPE,
            encoding="utf-8",
            check=True,
        )
        with open(html_path, encoding="utf-8", mode="w") as fh:
            fh.write(md_subber.sub(r'href="\1.html"', result.stdout))

    return run


builders = {
    "pandoc": pandoc_build,
    "lowdown": lowdown_build,
}


def main():
    opts, args = getopt.getopt(
        args=sys.argv[1:],
        shortopts="r:m:t:o:",
        longopts=["root=", "config=", "theme=", "out="],
    )
    if len(args) > 0:
        sys.exit("error: no arguments are allowed")
    root_path = None
    config_path = None
    theme_path = None
    out_path = None
    for opt, value in opts:
        if opt in ("-r", "--root"):
            root_path = value
        if opt in ("-m", "--config"):
            config_path = value
        elif opt in ("-t", "--theme"):
            theme_path = value
        elif opt in ("-o", "--out"):
            out_path = value

    config = {}
    if config_path is not None:
        with open(config_path) as fh:
            config = json.load(fh)
        if not isinstance(config, dict):
            sys.exit("error: config must be a dictionary")
        config_base = path.dirname(config_path)
        if root_path is None:
            root_path = config.get("root", path.join(config_base, "src"))
        if theme_path is None and "theme" in config:
            theme_path = path.normpath(path.join(config_base, config["theme"]))

    ensure_dir(root_path)
    ensure_dir(theme_path, "specify a theme directory with --theme=")
    ensure_dir(out_path, "specify an output directory with --out=")
    template_path = path.join(theme_path, "main.html")
    if not path.isfile(template_path):
        sys.exit(f"error: cannot find '{template_path}'")

    builder_name = config.get("builder", "pandoc")
    make_build = builders.get(builder_name)
    if make_build is None:
        sys.exit(f"error: no such builder: {builder_name}")

    print("Copying from:", theme_path, file=sys.stderr)
    copytree(theme_path, out_path, "*.html")

    print("Copying from:", root_path, file=sys.stderr)
    copytree(root_path, out_path, "*.md")

    build = make_build(path.dirname(sys.argv[0]), config, template_path)

    for dirpath, dirnames, filenames in os.walk(root_path):
        dirpath = path.relpath(dirpath, root_path)
        os.makedirs(dirpath, exist_ok=True)
        for filename in filenames:
            if filename.endswith(".md"):
                md_path = path.join(root_path, dirpath, filename)
                html_path = path.join(
                    out_path,
                    dirpath,
                    filename.removesuffix(".md") + ".html",
                )
                print("Generating:", path.join(dirpath, filename), file=sys.stderr)
                build(html_path, md_path)

    sys.exit(0)


if __name__ == "__main__":
    main()
