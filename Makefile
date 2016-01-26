# file: Makefile	G. Moody	23 August 2005
#			Last revised:	 12 July 2011
# 'make' description file for building WFDB wrappers with SWIG

# Change this if you did not do a standard installation of WFDB (if
# wfdb.h is not in /usr/include/wfdb/).
MAKE = make WFDB_HOME=/usr

all:	perl python java # csharp

install:
	-( cd wfdb-java;   $(MAKE) install )
	-( cd wfdb-perl;   $(MAKE) install )
	-( cd wfdb-python; $(MAKE) install )
#	-( cd wfdb-csharp; $(MAKE) install )
#	-( cd wfdb-octave; $(MAKE) install )

check:
	-( cd wfdb-java;   $(MAKE) check )
	-( cd wfdb-perl;   $(MAKE) check )
	-( cd wfdb-python; $(MAKE) check )
#	-( cd wfdb-csharp; $(MAKE) check )
#	-( cd wfdb-octave; $(MAKE) check )

clean:
	-( cd wfdb-java;   $(MAKE) clean )
	-( cd wfdb-perl;   $(MAKE) clean )
	-( cd wfdb-python; $(MAKE) clean )
#	-( cd wfdb-csharp; $(MAKE) clean )
#	-( cd wfdb-octave; $(MAKE) clean )

java:
	-( cd wfdb-java;   $(MAKE) )

perl:
	-( cd wfdb-perl;   $(MAKE) )

python:
	-( cd wfdb-python; $(MAKE) )

# csharp needs work!
csharp:
	-( cd wfdb-csharp; $(MAKE) )

# octave: not implemented yet
octave:
	-( cd wfdb-octave;   $(MAKE) )
