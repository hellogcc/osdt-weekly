no-op:
	echo "type an action: index, push"

index:
	cd weekly && ls -1 -r | sed 's,\(^.*\).md,- [\1 第080期](weekly/\1.md),'

push:
	git remote | xargs -I{} git push {} master

.PHONY: no-op index push
