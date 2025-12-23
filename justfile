[private]
@default:
	@just --list

# run the deployment playbook for a given site
deploy site:
	cd {{site}} && find . -name \*.orig -delete && ansible-playbook --ask-vault-password -i ../hosts.ini --diff deploy.yml

# do a local build of a site with mkdocs
build site:
	cd {{site}} && mkdir -p output && mkdocs build -d output

# install the tooling
tools:
    uv tool install mkdocs --with mkdocs-awesome-pages-plugin
