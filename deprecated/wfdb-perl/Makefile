# file: Makefile	G. Moody		10 March 2006
#			Last revised:		 6 April 2006

all:		generated-makefile wfdb_perl_wrap.c
	$(MAKE) -f generated-makefile

install:	generated-makefile wfdb_perl_wrap.c
	$(MAKE) -f generated-makefile install

check:
	@perl ../examples/psamples.pl >check.out
	@if ( diff -q check.out ../examples/psamples.out ) \
	 then echo "Passed"; else echo "Failed"; fi

wfdb_perl_wrap.c:	../wfdb.i
	swig -I/usr/include -perl5 -outdir . -o wfdb_perl_wrap.c ../wfdb.i

clean:		generated-makefile
	mv Makefile save-makefile
	$(MAKE) -f generated-makefile clean
	rm -rf check.out gen* Makefile.old perl.bs swig-version wfdb* *~
	mv save-makefile Makefile

generated-makefile:	Makefile.PL
	@-mkdir gen
	cp -p Makefile.PL gen
	cd gen; perl Makefile.PL
	mv gen/Makefile generated-makefile
