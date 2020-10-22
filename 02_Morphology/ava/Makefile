all:
	hfst-lexc ava.lexc -o ava.lexc.hfst
	hfst-twolc ava.twol -o ava.twol.hfst
	hfst-compose-intersect -1 ava.lexc.hfst -2 ava.twol.hfst -o ava.gen.hfst
	hfst-minimise ava.gen.hfst  | hfst-fst2txt | python3 att2dot.py  | dot -Tpng -oava.gen.png
	open ava.gen.png
