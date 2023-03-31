#!/usr/bin/env python

import os
import platform
import numpy
from setuptools import setup, Extension

intimg_version = os.environ.get('VERSION')
if not intimg_version:
    raise ValueError("VERSION environment variable is not set.")

numpy_include_path = numpy.get_include()
library_include_path = "/path/to/library/include"
library_lib_path = "/path/to/library/lib"
extra_include_dirs = [os.path.join("..", "Core"),
                      os.path.join("..", "Core", "functions_CPU"),
                      "."]
if platform.system() == 'Windows':
    compile_args = ['/DWIN32', '/EHsc', '/DBOOST_ALL_NO_LIB', '/openmp']
else:
    compile_args = ['-fopenmp', '-O2', '-funsigned-char', '-Wall', '-std=c++0x']
    extra_libraries = ['omp']

extra_include_dirs += [numpy_include_path, library_include_path]
extra_library_dirs = [library_lib_path]

extension = Extension(name="",
                      sources=[os.path.join(".", "src", "cpu_wrappers.pyx")],
                      include_dirs=extra_include_dirs,
                      library_dirs=extra_library_dirs,
                      extra_compile_args=compile_args,
                      libraries=['intimg'])

setup(
    version=intimg_version,
    ext_modules=[extension],
    zip_safe=False,
    packages=['intimg', 'intimg.supp']
)
