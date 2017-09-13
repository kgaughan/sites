DOMAIN_NAME:=mirrors.talideon.com
DEST:=manann.talideon.com

deploy:
	ansible-playbook -i $(DEST), -e domain_name=$(DOMAIN_NAME) deploy.yml

.PHONY: deploy
