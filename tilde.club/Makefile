deploy: build
	rsync -avz --delete-after site/ tilde.club:public_html

build:
	mkdocs build --strict --site-dir site

.PHONY: build deploy
