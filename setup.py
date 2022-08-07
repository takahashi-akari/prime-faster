# primes - Faster Prime Number Generator
# Author: Takahashi Akari <akaritakahashioss@gmail.com>
# License: MIT License (https://opensource.org/licenses/MIT)
# Version: 0.0.1
# Date: 2022-08-08
# Python: 3.10.6
# Description: primes - Faster Prime Number Generator

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="primes",
    version="0.0.1",
    author="Takahashi Akari",
    author_email="akaritakahashioss@gmail.com",
    description="primes - Faster Prime Number Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/takahashi-akari/primes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
