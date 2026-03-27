#!/bin/sh

set -eu

site_path="${1:-}"
if test -z "$site_path"; then
	echo "error: specify a path to a site directory" 2>&1
	exit 64
fi

out_dir="$(mktemp -d)"
trap "rm -rf '$out_dir'" EXIT

./build.py --out="$out_dir" --config="$site_path/build.json"

eval $(jq -r '@sh "host=\(.host) remote_path=\(.remote_path)"' "$site_path/build.json")

rsync -P -rvczz --delete --exclude=.DS_Store --exclude='.*.sw?' --cvs-exclude "$out_dir/" "keith@$host:$remote_path"
