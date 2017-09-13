DOMAIN_NAME:=mirrors.talideon.com
DEST:=manann.talideon.com

deploy:
	ansible-playbook -i $(DEST), \
		-e domain_name=$(DOMAIN_NAME) \
		-e tls_domain=talideon.com \
		deploy.yml

.PHONY: deploy
