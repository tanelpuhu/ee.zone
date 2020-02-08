all: git fetch commit

git:
	git checkout master
	git config --local user.name 'github-action'
	git config --local user.email 'github-action@lusikas.com'

fetch:
	dig @zone.internet.ee ee. axfr > zone.ee.tmp
	python task.py zone.ee.tmp zone.ee
	rm zone.ee.tmp

commit:
	git add zone.ee Makefile
	git commit --allow-empty -m "update at $(shell date)"
	git push -f -q https://$(TOKEN)@github.com/tanelpuhu/ee.zone.git master
