
%include javadoc.i

%pragma(java) jniclassimports=%{
 import java.util.LinkedList;
%}

%pragma(java) jniclasscode=%{
  static {
        
	boolean jniNotLoaded = true;

        try {
                System.loadLibrary("wfdbjava");
                jniNotLoaded = false;
        } catch (UnsatisfiedLinkError e) {
                System.err.println("System.loadLibrary('wfdbjava') failed, trying System.load()");
        }

        // Load the correct jni shared library for the platform, or die trying

        String osName = System.getProperty("os.name");  // the os we are running on (Windows, Mac, or Linux)
	LinkedList<String> jniLibPaths = new LinkedList<String> ();  // List of paths to check

	if (System.getProperty("java.library.path") != null ) {
	  // if the java.library.path property is set, make that the first path to check
	  for ( String p : System.getProperty("java.library.path").split("[:;]") ) {
	    jniLibPaths.add(p); 
	  }       
	}
	String jniLibName;
	if ( osName.indexOf("Linux") > -1 ) {
	    jniLibName = "libwfdbjava.so";
            // Some locations to try on Linux
	    jniLibPaths.add("/usr/local/lib");
	    jniLibPaths.add("/usr/lib");
	    jniLibPaths.add("/opt/wfdb/lib");
	    jniLibPaths.add("/usr/local/lib64");
	    jniLibPaths.add("/usr/lib64");
	    jniLibPaths.add("/opt/wfdb/lib64");
	} else if ( osName.indexOf("Windows") > -1 ) {
	    jniLibName = "wfdbjava.dll";
            // Some locations to try on Windows
	    jniLibPaths.add("c:\\wfdb\\lib");
	    jniLibPaths.add("c:\\cygwin\\wfdb\\lib");
	    jniLibPaths.add("c:\\Program Files\\wfdb\\lib");
	    jniLibPaths.add("c:\\system32");
	} else if ( osName.indexOf("Mac OS X") > -1 ) {	  
	    jniLibName = "libwfdbjava.dylib";	    
            // Some locations to try on Mac
	    jniLibPaths.add("/opt/wfdb/lib");
	    jniLibPaths.add("/opt/local/lib");
	    jniLibPaths.add("/usr/lib");
	    jniLibPaths.add("/usr/local/lib");
	} else {
	    jniLibName = "libwfdbjava.so"; // Solaris and BSD use .so, 
	                                          // does any other OS matter
	    // you'll have to use java.library.path on these platforms
	}

	String sysLibraryPath = jniLibPaths.poll(); // get the first path
	while ( jniNotLoaded & sysLibraryPath != null ) {
	  try {
	      //System.err.println("Trying to load " + jniLibName + " from " + sysLibraryPath);
	      System.load(sysLibraryPath+"/"+jniLibName);
	      jniNotLoaded = false; // this line will be reached only if System.load works
	  } catch (UnsatisfiedLinkError e) {
	    sysLibraryPath = jniLibPaths.poll(); // try the next path	   
	  }
	}

	if (jniNotLoaded) {
	      // oh, no the jni library did not load!
	      System.err.println();
	      System.err.println("Error: Could not load wfdb wrappers");
	      System.err.println("no " + jniLibName + " in java.library.path="+sysLibraryPath);
	      //System.err.println(osName);
	      System.exit(1);
	}          

  }

%}
