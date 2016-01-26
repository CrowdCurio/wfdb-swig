
%{
#define SWIG_FILE_WITH_INIT
%}
%include "numpy.i"
%init %{
import_array();
%}

/* Typemaps for mapping WFDB_Sample vector to 1-D Numpy Array ARGOUT */
%typemap(in,numinputs=0,
	 fragment="NumPy_Backward_Compatibility,NumPy_Macros")
    (WFDB_Sample *WFDB_SAMPLE_ARRAY1)
    (PyObject * array = NULL)
{
  npy_intp dims[1] = { spy_nvsig() };
  array = PyArray_SimpleNew(1, dims, NPY_INT);
  if (!array) SWIG_fail;
  $1 = ($1_ltype) array_data(array);
}

%typemap(argout) 
  (WFDB_Sample *WFDB_SAMPLE_ARRAY1)
{
  $result = SWIG_Python_AppendOutput($result,array$argnum);
}

/* Typemaps for mapping WFDB_Sample vector to 2-D Numpy Array ARGOUT */
%typemap(in,numinputs=1,
	 fragment="NumPy_Fragments")
  (WFDB_Sample *WFDB_SAMPLE_ARRAY2, int DIM2)
  (PyObject * array = NULL)
{
  npy_intp dims[2];
  int tmp;

  if (!PyInt_Check($input))
  {
  const char* typestring = pytype_string($input);
  PyErr_Format(PyExc_TypeError,
	       "Int dimension expected.  '%s' given.",
	       typestring);
  SWIG_fail;
  }

  tmp = (npy_intp) PyInt_AsLong($input);

  if ( tmp < 1 )
      $2 = dims[0] = spy_nsamps();
  else
      $2 = dims[0] = tmp;

  dims[1] = spy_nvsig();
  array = PyArray_SimpleNew(2, dims, NPY_INT);
  if (!array) SWIG_fail;
  $1 = ($1_ltype) array_data(array);
}


%typemap(argout) 
(WFDB_Sample *WFDB_SAMPLE_ARRAY2, int DIM2)
{

  $result = SWIG_Python_AppendOutput($result,array$argnum);
}

/* Typemaps for mapping double vector to 2-D Numpy Array ARGOUT */
%typemap(in,numinputs=1,
	 fragment="NumPy_Fragments")
  (double *DOUBLE_ARRAY2, int DIM2)
  (PyObject * array = NULL)
{
  npy_intp dims[2];
  int tmp;
  
  if (!PyInt_Check($input))
  {
  const char* typestring = pytype_string($input);
  PyErr_Format(PyExc_TypeError,
	       "Int dimension expected.  '%s' given.",
	       typestring);
  SWIG_fail;
  }

  tmp = (npy_intp) PyInt_AsLong($input);
  if ( tmp < 1 )      
      $2 = dims[0] = spy_nsamps();
  else
      $2 = dims[0] = tmp;

  dims[1] = spy_nvsig();
  array = PyArray_SimpleNew(2, dims, NPY_DOUBLE);
  if (!array) SWIG_fail;
  $1 = ($1_ltype) array_data(array);
}


%typemap(argout)
(double *DOUBLE_ARRAY2, int DIM2)
{
  $result = SWIG_Python_AppendOutput($result,array$argnum);
}


%apply (WFDB_Sample *WFDB_SAMPLE_ARRAY1) { (WFDB_Sample *vector) }
%apply (WFDB_Sample *WFDB_SAMPLE_ARRAY2, int DIM2) { (WFDB_Sample *vector, int nsamples) }
%apply (double *DOUBLE_ARRAY2, int DIM2) { (double *vector, int nsamples) }


%pythoncode %{

def isigopen(record):
  nsig = _wfdb.isigopen(record, None, 0)  
  if nsig > 0:
      siArray = WFDB_SiginfoArray(nsig)
      _wfdb.isigopen(record, siArray.cast(), nsig)
      siArray.nsig = nsig
      set_nvsig(nsig)
      set_nsamps(siArray[0].nsamp)
  else:
      siArray = None
  return siArray

%}


