rm -f psi-k_highlight.aux psi-k_highlight.toc psi-k_highlight.blg psi-k_highlight.bbl psi-k_highlight.log
pdflatex psi-k_highlight.tex 
bibtex psi-k_highlight
pdflatex psi-k_highlight.tex 
pdflatex psi-k_highlight.tex
bibtex psi-k_highlight
pdflatex psi-k_highlight.tex
