#!/usr/bin/env python

import setuptools
from distutils.core import setup
import os
import numpy
import platform
import sys
intimg_version=os.environ['VERSION']

dir= [numpy.get_include(), library_include_path]
compile = []
extra = [library_lib_path]
arguments = []
link = []
extra_libraries = ['intimg']

print ("extra_library_dirs " , extra_library_dirs)

extra_include_dirs += [os.path.join(".." , "Core"),
                       os.path.join(".." , "Core",  "functions_CPU"),
						   "."]

if platform.system() == 'Windows':
    compile[0:] = ['/DWIN32','/EHsc','/DBOOST_ALL_NO_LIB' , '/openmp' ]
else:
    extra_compile_args = ['-fopenmp','-O2', '-funsigned-char', '-Wall', '-std=c++0x']
    extra_libraries += [@EXTRA_OMP_LIB@]

setup(
    version=intimg_version,
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("",
                             sources=[os.path.join("." , "src", "cpu_wrappers.pyx") ],
                             include_dirs=extra,
			     library_dirs=dir,
        		     extra_compile_args=extra_compile_args,
			     libraries=extra_libraries ),

    ],
	zip_safe = False,
	packages=['intimg', 'intimg.supp'],
)
