EXTRA_DIST = \
	wfdb-csharp.snk

lib_LTLIBRARIES = libwfdbcsharpglue.la
libwfdbcsharpglue_la_SOURCES = wfdb_csharp_wrap.c wfdb.h
libwfdbcsharpglue_la_LDFLAGS = -version-info "10:4:0" -lwfdb

ASSEMBLY_NAME = wfdb-csharp
references =

TARGET = $(ASSEMBLY)
ASSEMBLY = $(ASSEMBLY_NAME).dll
noinst_DATA = $(ASSEMBLY)
CLEANFILES = $(ASSEMBLY) wfdb-csharp.snk
DISTCLEANFILES = 

sources = \
	wfdb/SWIGTYPE_p_int.cs \
	wfdb/SWIGTYPE_p_p_char.cs \
	wfdb/WFDB_SampleArray.cs \
	wfdb/WFDB_AnninfoArray.cs \
	wfdb/WFDB_Anninfo.cs \
	wfdb/WFDB_Annotation.cs \
	wfdb/WFDB_Calinfo.cs \
	wfdb/wfdb.cs \
	wfdb/wfdbPINVOKE.cs \
	wfdb/WFDB_SiginfoArray.cs \
	wfdb/WFDB_Siginfo.cs

$(ASSEMBLY): $(sources) wfdb-csharp.snk
	$(CSC) /unsafe /out:$(ASSEMBLY) /target:library /keyfile:wfdb-csharp.snk $(references) $(sources)


#install-data-local:
install-data-hook:
	@if test -n '$(TARGET)'; then \
	  echo "$(GACUTIL) /i $(ASSEMBLY) /f $(GACUTIL_FLAGS)"; \
	  $(GACUTIL) /i $(ASSEMBLY) /f $(GACUTIL_FLAGS) || exit 1; \
	fi

uninstall-local:
	@if test -n '$(TARGET)'; then \
	  echo "$(GACUTIL) /u $(ASSEMBLY_NAME) $(GACUTIL_FLAGS)";       \
	  $(GACUTIL) /u $(ASSEMBLY_NAME) $(GACUTIL_FLAGS) || exit 1;    \
	fi
