# file: Makefile	G. Moody	12 March 2006
#
# Makefile for building the example Java programs

SOURCES=example1.java example2.java example3.java example4.java example5.java \
	example6.java example7.java example9.java example10.java \
	psamples.java rdsamp.java rdann.java

# This Makefile can be used to create either standalone programs or .class
# files.  The difference is that standalone programs contain opcodes that your
# CPU can execute directly, and .class files contain Java bytecodes that must
# be interpreted at run time by a Java virtual machine (JVM).
#
# If you wish to create standalone programs with gcj, uncomment the next line.
PROGRAMS = $(SOURCES:.java=)
# Otherwise, uncomment the next line to create .class files with javac.
# PROGRAMS = $(SOURCES:.java=.class)
# If you create .class files, they can be run using the 'jw' shell script
# in this directory, like this:
#	./jw example1
# Read the comments in 'jw' to see how this works.

WFDBJAR=/usr/share/java/wfdb.jar

all:	 $(PROGRAMS)

%.class : %.java
	javac -cp $(WFDBJAR):. $<

% : %.java
	-gcj -fjni -I$(WFDBJAR) --main=$@ $< $(WFDBJAR)
	-mv a.out $@

clean:
	rm -f $(PROGRAMS) *~

