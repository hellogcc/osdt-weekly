booknotes bn:
	grep -r '^本周推荐' weekly-* | sort | tail -n 50

push:
	git remote | xargs -I{} git push {} master

# ---- 网站（osdtweekly.com） ----
# 期号页面由 scripts/gen_issues.py 生成，故所有站点目标都先跑一遍生成
site:
	python3 scripts/gen_issues.py
	hugo --source website --gc --minify

site-serve:
	python3 scripts/gen_issues.py
	hugo server --source website --buildFuture --disableFastRender --port 1313

site-check: site
	python3 scripts/check_site.py

site-clean:
	rm -rf website/public website/resources website/content/issue website/data/issues.yaml website/static/images

help:
	@echo "type an action:"
	@echo "  bn          往期「本周推荐」汇总"
	@echo "  push        推送到所有远端"
	@echo "  site        生成期号页面并构建到 website/public"
	@echo "  site-serve  本地预览 http://localhost:1313/"
	@echo "  site-check  构建后自检站内链接、期号完整性、RSS"
	@echo "  site-clean  清掉站点构建产物与生成内容"

.PHONY: help push booknotes bn site site-serve site-check site-clean
