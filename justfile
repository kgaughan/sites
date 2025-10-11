@default:
	@just --list

deploy site:
	cd {{site}} && find . -name \*.orig -delete && ansible-playbook -i ../hosts.ini --diff deploy.yml

build site:
	cd {{site}} && mkdir -p output && mkdocs build -d output
