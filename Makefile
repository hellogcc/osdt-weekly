booknotes bn:
	grep -r '^本周推荐' weekly-* | sort | tail -n 50

push:
	git remote | xargs -I{} git push {} master

help:
	echo "type an action: bn, push"

.PHONY: help push booknotes bn
