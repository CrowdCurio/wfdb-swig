
AC_INIT(wfdb-csharp, 10.4)
AC_CANONICAL_SYSTEM
AM_INIT_AUTOMAKE

dnl Checks for programs.
AC_PROG_INSTALL
AC_PROG_CC
AM_PROG_LIBTOOL


dnl Mono checks, lifted from gtk-sharp's configure.in
MONO_REQUIRED_VERSION=0.96
PKG_CHECK_MODULES(MONO_DEPENDENCY, mono >= $MONO_REQUIRED_VERSION, has_mono=true, has_mono=false)

if test "x$has_mono" = "xtrue"; then
GACUTIL_FLAGS='/package $(PACKAGE) /gacdir $(DESTDIR)$(libdir)'
GENERATED_SOURCES=generated/*.cs
AC_PATH_PROG(RUNTIME, mono, no)
AC_PATH_PROG(CSC, mcs, no)
if test `uname -s` = "Darwin"; then
        LIB_PREFIX=
        LIB_SUFFIX=.dylib
else
        LIB_PREFIX=.so
        LIB_SUFFIX=
fi
else
AC_PATH_PROG(CSC, csc.exe, no)
GACUTIL_FLAGS=
GENERATED_SOURCES=generated\\\\*.cs

if test x$CSC = "xno"; then
        AC_MSG_ERROR([You need to install either mono or .Net])
else
RUNTIME=
LIB_PREFIX=
LIB_SUFFIX=.dylib
fi
fi

CS="C#"
if test "x$CSC" = "xno" ; then
        AC_MSG_ERROR([No $CS compiler found])
fi

AC_PATH_PROG(GACUTIL, gacutil, no)
if test "x$GACUTIL" = "xno" ; then
        AC_MSG_ERROR([No gacutil tool found])
fi

AC_SUBST(RUNTIME)
AC_SUBST(CSC)
AC_SUBST(GACUTIL)
AC_SUBST(GACUTIL_FLAGS)
AC_SUBST(LIB_PREFIX)
AC_SUBST(LIB_SUFFIX)
AC_SUBST(GENERATED_SOURCES)


AC_CONFIG_FILES([Makefile 
		 wfdb-csharp.spec])
AC_OUTPUT
