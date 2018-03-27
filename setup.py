""" readExcel Python Project with Pandas"""

# Prefer setuptools over disutils
from setuptools import setup, find_packages

#For consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='influencer-report',
    version='1.0.0',
    description='Aggregates the multi-tabbed influencer report excel sheets into a digestible json list',
    author="James O'Brien",
    author_email="james@oneriossolutions.com",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Data Scientists',
        'Programming Language :: Python :: 3.6'
                 ],
    py_modules=[''],
    install_requires=['wheel', 'pandas'],
    python_requires='>=3'
)
