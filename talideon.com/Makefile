all:

deploy:
	ansible-playbook -i hosts.ini --diff \
		-e @secrets.yml $(if $(wildcard ./vault-password),--vault-password-file=./vault-password,--ask-vault-pass) \
		deploy.yml
