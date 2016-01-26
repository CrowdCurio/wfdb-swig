# file: Makefile	G. Moody	12 July 2011
#
# Makefile for building the example Java programs

SOURCES=example1.java example2.java example3.java example4.java example5.java \
	example6.java example7.java example9.java example10.java \
	psamples.java rdsamp.java rdann.java

# This Makefile can be used to create either standalone programs or .class
# files.  The difference is that standalone programs contain opcodes that your
# CPU can execute directly, and .class files contain Java bytecodes that must
# be interpreted at run time by a Java virtual machine (JVM).

# Uncomment one of the next two lines:
JAVAC=javac
# JAVAC=gcj

GCJPROGS = $(SOURCES:.java=)
JAVACPROGS = $(SOURCES:.java=.class)

# If you create .class files, they can be run using the 'jw' shell script
# in this directory, like this:
#	./jw example1
# Read the comments in 'jw' to see how this works.

WFDBJAR=/usr/share/java/wfdb.jar

all:
	if [ $(JAVAC) = gcj ]; then $(MAKE) $(GCJPROGS); else $(MAKE) $(JAVACPROGS); fi

%.class : %.java
	javac -cp $(WFDBJAR):. $<

% : %.java
	-gcj -fjni -I$(WFDBJAR) --main=$@ $< $(WFDBJAR)
	-mv a.out $@

clean:
	rm -f $(GCJPROGS) $(JAVACPROGS) *~

