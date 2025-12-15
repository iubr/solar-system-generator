from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "pysolsys.cintegrate",
        sources=["pysolsys/cintegrate_wrapper.pyx", "pysolsys/cintegrate.cpp"],
        include_dirs=["pysolsys"],
        language="c++",
    )
]

setup(ext_modules=cythonize(ext_modules, language_level=3))
