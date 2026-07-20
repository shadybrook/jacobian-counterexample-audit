.PHONY: verify test paper clean

PYTHON ?= python3

verify:
	$(PYTHON) src/verify.py

test:
	$(PYTHON) -m pytest -q

paper:
	LC_ALL=C LANG=C latexmk -pdf -interaction=nonstopmode -halt-on-error \
		-jobname=jacobian_counterexample_audit -output-directory=output/pdf paper/main.tex

clean:
	LC_ALL=C LANG=C latexmk -C -jobname=jacobian_counterexample_audit \
		-output-directory=output/pdf paper/main.tex 2>/dev/null || true
