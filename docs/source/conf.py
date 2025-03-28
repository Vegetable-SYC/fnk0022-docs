# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
from datetime import datetime
import os
import pathlib
import sys

sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

os.system("rm -r freenove_Kit")
os.system("git clone --depth 1 https://github.com/Freenove/Freenove_Basic_Starter_Kit_for_Raspberry_Pi freenove_Kit")

project = "fnk0066-docs"
# <!!!BEGIN!!!>
# <!!!END!!!>