from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.extension import Extension
import sys
missing_modules = []
INSTALL_ERROR   = False

# Try importing necessary modules to test
# and see if they are installed.
try:
    from Cython.Build import cythonize
except ImportError:
    missing_modules.append('cython')

try:
    import numpy
except ImportError:
    missing_modules.append('numpy')

try:
    import scipy
except ImportError:
    missing_modules.append('scipy')

try:
    import pandas
except ImportError:
    missing_modules.append('pandas')

try:
    import matplotlib
except ImportError:
    missing_modules.append('matplotlib')

try:
    import seaborn
except ImportError:
    missing_modules.append('seaborn')

try:
    import multiprocess
except ImportError:
    print("\n'multiprocess' module not found.\n\n  Install with: pip install multiprocess")

if len(missing_modules) > 0:
    INSTALL_ERROR = True
    print("\nERROR:")
    print("  You are missing the following required modules:")
    for m in missing_modules:
        print("  \t", m)
    print("\n")

if INSTALL_ERROR:
    print("\nERROR:")
    print("  Unable to install phyde.")
    print("  Please see the documentation at http://hybridization-detection.rtfd.io/.\n")
    sys.exit(-1)
else:
    setup(
        name="phyde",
        version="0.4.0",
        description="Hybridization detection using phylogenetic invariants",
        long_description=open('README.rst').read(),
        url="https://github.com/pblischak/HyDe",
        author="Paul Blischak & Laura Kubatko",
        author_email="blischak.4@osu.edu",
        packages=find_packages(),
        ext_modules=cythonize([Extension("phyde.core.data", ["phyde/core/data.pyx"],
                                         include_dirs=[numpy.get_include()],
                                         language="c++"),]),
        #include_dirs=[numpy.get_include()],
        scripts=[
            'scripts/run_hyde.py',
            'scripts/run_hyde_mp.py',
            'scripts/individual_hyde.py',
            'scripts/individual_hyde_mp.py',
            'scripts/bootstrap_hyde.py',
            'scripts/bootstrap_hyde_mp.py'
        ],
        license="GPLv3",
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Cython',
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
        ],
        zip_safe=False
    )
