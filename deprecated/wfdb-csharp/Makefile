# file: Makefile	G. Moody		6 April 2006

all:
	cp -pr conf build
	cp -p ../AUTHORS ../ChangeLog ../COPYING ../INSTALL ../NEWS ../README \
	  build
	swig -I/usr/include -csharp -namespace Wfdb -dllimport wfdbcsharpglue \
	  -outdir build/wfdb -o build/wfdb_csharp_wrap.c ../wfdb.i
	cd build; ./acgen.sh
	cd build; ./configure --prefix=/usr CFLAGS="-O1"
	cd build; $(MAKE)

install:
	cd build; $(MAKE) install

check:
	cp ../examples/*.cs examples
	cd examples; $(MAKE)
	examples/csw examples/psamples >check.out
	@if ( diff -q check.out ../examples/psamples.out ) \
	 then echo "Passed"; else echo "Failed"; fi

rpm:
	$(MAKE) all
	mv build wfdb-csharp
	tar cfvz wfdb-csharp.tar.gz wfdb-csharp/
	rpmbuild -ta wfdb-csharp.tar.gz
	mv wfdb-csharp build

clean:
	cd examples; $(MAKE) clean
	rm -rf build check.out examples/*.cs wfdb-csharp.tar.gz *~


