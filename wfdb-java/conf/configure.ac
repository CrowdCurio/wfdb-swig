AC_INIT(wfdb-java, 10.5)
AC_CONFIG_MACRO_DIR([m4])
AC_CANONICAL_SYSTEM
AM_INIT_AUTOMAKE

dnl Checks for programs.
AC_PROG_INSTALL
AC_PROG_CC
AM_PROG_LIBTOOL
AX_JNI_INCLUDE_DIR
for JNI_INCLUDE_DIR in $JNI_INCLUDE_DIRS
do
	CPPFLAGS="$CPPFLAGS -I$JNI_INCLUDE_DIR"
done

AX_CHECK_CLASSPATH
AX_PROG_JAVAC
AX_PROG_JAR

AM_CONDITIONAL([BUILD_JAVA], [test "x$JAVA_CC" != x])

AC_ARG_WITH([jardir], AS_HELP_STRING([--with-jardir],
                      [where to install jar files]),
            [jardir="$with_jardir"], [jardir="${datadir}/java"])
AC_SUBST(jardir)


AC_CONFIG_FILES([Makefile 
		 wfdb-java.spec])
AC_OUTPUT
