BASEDIR:=$(PWD)
OUTPUTDIR:=$(PWD)/output

all:

publish:
	mkdir -p $(OUTPUTDIR)
	mkdocs build -d $(OUTPUTDIR)

upload: publish
	rsync -P -rvczz --delete --exclude=.DS_Store --exclude='.*.sw?' --cvs-exclude $(OUTPUTDIR)/ keith@lir.talideon.com:/usr/local/www/talideon.com/web

deploy:
	ansible-playbook -i ../hosts.ini --diff \
		-e @secrets.yml $(if $(wildcard ./vault-password),--vault-password-file=./vault-password,--ask-vault-pass) \
		deploy.yml

.PHONY: all publish upload deploy
