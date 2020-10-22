all:
	hfst-lexc fin.lexc -o fin.lexc.hfst
	hfst-minimise fin.lexc.hfst | hfst-fst2txt | python3 att2dot.py | dot -Tpng -ofin.gen.png
	open fin.gen.png
