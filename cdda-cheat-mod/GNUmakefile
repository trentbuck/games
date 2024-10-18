# https://ruudvanasseldonk.com/2023/01/11/the-yaml-document-from-hell
# https://hitchdev.com/strictyaml/why/implicit-typing-removed/
# https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
# https://jinja.palletsprojects.com/templates/
# https://yaml.org/spec/1.1/spec.pdf
all: $(patsubst %.yaml,%.json,$(wildcard [a-z]*.yaml))
%.json: %.yaml
	yq . $< >/dev/null	# don't save file if has errors
	yq . $< >$@
clean distclean:
	rm -f *.json
.PHONY: all clean
