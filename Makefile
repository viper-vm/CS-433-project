PY := python3

all: s d

s:
	$(PY) schema.py

d: 
	$(PY) demo.py