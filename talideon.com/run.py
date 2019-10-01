#!/usr/bin/env python3

import argparse
import os

from cheroot import wsgi

from komorebi.app import app


def main():
    parser = argparse.ArgumentParser(description="Runs komorebi.")
    parser.add_argument(
        "--unix", help="Path to Unix domain socket", default="/var/run/komorebi.sock"
    )
    args = parser.parse_args()

    # This is a hack until I can find a better way to do the cleanup.
    if os.path.exists(args.unix):
        os.unlink(args.unix)

    wsgi.Server(args.unix, app.wsgi_app).start()


if __name__ == "__main__":
    main()
