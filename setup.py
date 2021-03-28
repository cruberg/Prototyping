import sys
import setuptools

with open('README.md', "r") as fh:
    long_description = fh.read()

install_requires = []

source_code_dir = "src"

setuptools.setup(
    name="Prototype",
    version="1.0.0",
    author="cruberg4",
    author_email="cruberg@protonmail.ch",
    description="Go fuck yourself",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(source_code_dir),
    package_dir={
        "": source_code_dir
    },
    install_requires= install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)