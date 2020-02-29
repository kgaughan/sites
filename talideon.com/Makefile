all:

deploy:
	ansible-playbook -i lir.talideon.com, \
		-e @secrets.yml $(if $(wildcard ./vault-password),--vault-password-file=./vault-password,--ask-vault-pass) \
		deploy.yml
