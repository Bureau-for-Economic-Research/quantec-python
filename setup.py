import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = "0.0.1"
PACKAGE_NAME = "quantec"
AUTHOR = "Hanjo Odendaal"
AUTHOR_EMAIL = "hanjo@sun.ac.za"
URL = "XXX"

LICENSE = "MIT"
DESCRIPTION = "Quantec API Python Package"
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
    "setuptools",
    "pandas",
    "pytest",
    "requests",
    "logger",
    "python-decouple==3.8",
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
)
