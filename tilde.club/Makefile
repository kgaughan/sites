deploy: build
	rsync -avz --exclude-from=../.gitignore --delete-after site/ tilde.club:public_html

build:
	mkdocs build --strict --site-dir site

serve:
	mkdocs serve --strict

.PHONY: build deploy serve
