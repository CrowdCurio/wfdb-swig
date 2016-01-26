# file: Makefile	G. Moody		10 March 2006
#			Last revised:		 6 April 2006


WFDB_HOME=/usr/local
WFDB_INCLUDE=$(WFDB_HOME)/include
WFDB_LIBPATH=$(WFDB_HOME)/lib

all:		setup.py wfdb_python_wrap.c
		WFDB_HOME=$(WFDB_HOME) CFLAGS=-I$(WFDB_INCLUDE) python setup.py build

install:	setup.py wfdb_python_wrap.c
		python setup.py install

check:
	@python ../examples/psamples.py >check.out
	@if ( diff -q check.out ../examples/psamples.out ) \
	 then echo "Passed"; else echo "Failed"; fi

wfdb_python_wrap.c:	../wfdb.i
	swig -I$(WFDB_INCLUDE) -python -outdir . -o wfdb_python_wrap.c ../wfdb.i

clean:
	python setup.py clean
	rm -rf  build check.out swig-version wfdb* *~
