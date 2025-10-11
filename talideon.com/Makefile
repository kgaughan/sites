BASEDIR:=$(PWD)
OUTPUTDIR:=$(PWD)/output

.PHONY: build
build:
	mkdir -p $(OUTPUTDIR)
	mkdocs build -d $(OUTPUTDIR)

.PHONY: upload
upload: build
	rsync -P -rvczz --delete \
		--exclude=.DS_Store \
		--exclude='.*.sw?' \
		--exclude='*.orig' \
		--cvs-exclude $(OUTPUTDIR)/ \
		keith@lir.talideon.com:/usr/local/www/talideon.com/web
