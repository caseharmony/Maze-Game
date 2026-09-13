from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

# Define the C++ extension
ext_modules = [
    Extension(
        name="cgrowing",        # The name of the compiled module to import in Python
        sources=["cgrowing.pyx"], # The name of your Cython source file
        language="c++",               # Required for libcpp (vector, pair, mt19937)
        include_dirs=[np.get_include()] # Required for 'cimport numpy'
    )
]

setup(
    ext_modules=cythonize(
        ext_modules,
        annotate=True,
        compiler_directives={
            'language_level': "3",    # Target Python 3
            'boundscheck': False,     # Disables array bounds checking
            'wraparound': False       # Disables negative index wrapping
        }
    )
)