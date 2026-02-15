from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

extensions_list = [
    Extension(
        "cdfs",                 
        sources=["cdfs.pyx"],
        language="c++",
        include_dirs=[np.get_include()]
    ),
    Extension(
        "prims",
        sources=["prims.pyx"],
        language="c++",
        include_dirs=[np.get_include()]
    ),
    Extension(
        "cbruteforce",
        sources=["cbruteforce.pyx"],
        language="c++",
        include_dirs=[np.get_include()]
    ),
]

setup(
    ext_modules = cythonize(
        extensions_list,
        compiler_directives={'language_level': "3"}
    )
)