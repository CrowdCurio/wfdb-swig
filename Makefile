# file: Makefile	G. Moody	23 August 2005
#			Last revised:	20 December 2011
# 'make' description file for building WFDB wrappers with SWIG

WFDB_HOME=/opt/wfdb

all:	python java 

install:
	-( cd wfdb-python; $(MAKE) install )
	-( cd wfdb-java;   $(MAKE) install )


check:
	-( cd wfdb-python; $(MAKE) check )
	-( cd wfdb-java;   $(MAKE) check )

python:
	-( cd wfdb-python; $(MAKE) )

java:
	-( cd wfdb-java;   $(MAKE) )


clean:
	-( cd wfdb-python; $(MAKE) clean )
	-( cd wfdb-java;   $(MAKE) clean )
	rm -f common/*~ *~

