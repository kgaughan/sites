mirrors:
	ansible-playbook -i manann.talideon.com, \
		-e domain_name=mirrors.talideon.com \
		deploy.yml

.PHONY: mirrors
