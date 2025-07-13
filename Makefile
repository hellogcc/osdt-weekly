no-op:
	echo "type an action: bn, push"

booknotes bn:
	grep -r '^本周推荐' weekly-* | sort | tail -n 20

push:
	git remote | xargs -I{} git push {} master

.PHONY: no-op push booknotes bn
