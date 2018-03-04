#!/bin/sh

here=$(dirname $0)

if [ -z "$1" ]; then
	echo "Please specify a domain." >&2
	exit 2
elif [ ! -e "$here/sites/$1/mkdocs.yml" ]; then
	echo "No such site: $1" >&2
	exit 2
fi

tmpdir=$(mktemp -d)
trap "rm -rf $tmpdir" EXIT

echo "==> Building..."
(cd "$here/sites/$1"; mkdocs build --strict --site-dir "$tmpdir")

echo "==> Syncing."
rsync --recursive --delete-after --exclude-from=exclusions --progress \
	"$tmpdir/" \
	"cian.talideon.com:sites/$1/web"
