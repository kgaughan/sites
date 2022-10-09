BASEDIR:=$(PWD)
OUTPUTDIR:=$(PWD)/output

all:

publish:
	mkdir -p $(OUTPUTDIR)
	mkdocs build -d $(OUTPUTDIR)

upload: publish
	rsync -P -rvczz --delete \
		--exclude=.DS_Store \
		--exclude='.*.sw?' \
		--exclude='*.orig' \
		--cvs-exclude $(OUTPUTDIR)/ \
		keith@lir.talideon.com:/usr/local/www/talideon.com/web

deploy:
	find . -name \*.orig -delete
	ansible-playbook -i ../hosts.ini --diff deploy.yml

.PHONY: all publish upload deploy
