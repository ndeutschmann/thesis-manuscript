LATEX=xelatex

LATEXMK=latexmk

MAIN=thesis

compile:
	$(LATEXMK) -$(LATEX) $(MAIN).tex

count:
	./scripts/updatecount
	./scripts/plot.py

clean:
	$(LATEXMK) -C $(MAIN)
	rm -f $(MAIN).pdfsync
	rm -f *~ *.tmp chapter[1-9]/*~
	rm -f *.bbl *.blg *.aux *.end *.fls *.log *.out *.fdb_latexmk

view:
	open $(MAIN).pdf

.PHONY: clean compile view count
