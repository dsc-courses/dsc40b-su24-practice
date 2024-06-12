.PHONY: html
html:
	practicebank build problems _build --template template.html
	cp style.css _build/style.css
