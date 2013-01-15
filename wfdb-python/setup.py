from setuptools import setup, Extension, find_packages
from numpy.distutils.misc_util import get_numpy_include_dirs
from os import getenv
 
WFDB_HOME= getenv('WFDB_HOME')

if WFDB_HOME is None:
    WFDB_HOME="/opt/wfdb"


module1 = Extension("_wfdb",
                    libraries = ["wfdb"],
		    library_dirs = [WFDB_HOME+"/lib",WFDB_HOME+"/lib64"],
                    include_dirs = [WFDB_HOME+"/include"] + get_numpy_include_dirs(),
                    sources = ['wfdb_python_wrap.c'])

setup (name = 'wfdb',
       version = '10.5',
       description = 'WFDB wrappers',
       author='I. Henry and G. Moody',
       author_email='wfdb-swig@physionet.org',
       url='http://physionet.org/physiotools/wfdb.shtml',
       py_modules = ["wfdb"],
       ext_modules = [module1],
       packages= find_packages())

