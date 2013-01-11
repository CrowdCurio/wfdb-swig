ACLOCAL_AMFLAGS = -I m4
JAVAC = @JAVAC@
JAR_TOOL = @jar_tool@
lib_LTLIBRARIES = libwfdbjava.la
libwfdbjava_la_SOURCES = wfdb_java_wrap.c
libwfdbjava_la_LDFLAGS = -version-info "10:4:0" -lwfdb -L$(libdir)

java_wfdb_source_files = \
	wfdb/SWIGTYPE_p_int.java \
	wfdb/SWIGTYPE_p_p_char.java \
	wfdb/WFDB_SampleArray.java \
	wfdb/WFDB_AnninfoArray.java \
	wfdb/WFDB_Anninfo.java \
	wfdb/WFDB_Annotation.java \
	wfdb/WFDB_Calinfo.java \
	wfdb/wfdbConstants.java \
	wfdb/wfdb.java \
	wfdb/wfdbJNI.java \
	wfdb/WFDB_SiginfoArray.java \
	wfdb/WFDB_Siginfo.java

wfdb_jardir = $(jardir)
wfdb_jar_DATA = wfdb.jar

wfdb_jar_class_files = $(java_wfdb_source_files:.java=.class)

$(wfdb_jar_class_files): %.class: %.java
	$(JAVAC) -classpath . -d . $< 

wfdb.jar : $(wfdb_jar_class_files)
	$(JAR) cf $@ $(wfdb_jar_class_files)

install-data-hook:
# install versionless jar symlink
	cd $(DESTDIR)$(wfdb_jardir) && \
		mv -f wfdb.jar wfdb-$(VERSION).jar && \
		$(LN_S) wfdb-$(VERSION).jar wfdb.jar

uninstall-local:
	-rm -f $(DESTDIR)$(wfdb_jardir)/wfdb-$(VERSION).jar

# clean files and directories
CLEANFILES = \
	$(wfdb_jar_class_files) \
	wfdb.jar
