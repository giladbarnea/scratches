from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(['example.pyx',        # Cython code file with primes() function
                           'example_py_compiled.py'],  # Python code file with primes_python_compiled() function
                          annotate=True),        # enables generation of the html annotation file
)