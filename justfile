[private]
@default:
	@just --list

# run the deployment playbook for a given site
deploy site:
	cd {{site}} && find . -name \*.orig -delete && ansible-playbook --ask-vault-password -i ../hosts.ini --diff deploy.yml

# do a local build of a site
build site:
	cd {{site}} && mkdir -p output && ../build.py --out=output --config=build.json

# serve a site locally
serve site: (build site)
	cd {{site}} && python3 -m http.server -d output
