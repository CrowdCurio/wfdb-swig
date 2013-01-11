# file: Makefile	G. Moody	6 April 2006
#
# Makefile for building the example C# programs

SOURCES=example1.cs example2.cs example3.cs example4.cs example5.cs \
	example6.cs example7.cs example9.cs example10.cs \
	psamples.cs rdsamp.cs rdann.cs

# The PROGRAMS created by running 'make' in this directory can be run using
# the 'csw' shell script in this directory, like this:
#	./csw example1
# Read the comments in 'csw' to see how this works.

PROGRAMS=example1.exe example2.exe example3.exe example4.exe example5.exe \
	example6.exe example7.exe example9.exe example10.exe \
	psamples.exe rdsamp.exe rdann.exe

# CSC is the C# bytecode compiler.
CSC = /usr/bin/mcs

all:	 $(PROGRAMS)

%.exe : %.cs
	$(CSC) /r:/usr/lib/mono/wfdb-csharp/wfdb-csharp.dll  $<

clean:
	rm -f $(PROGRAMS) *~

