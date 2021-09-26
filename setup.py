import pathlib
from setuptools import setup, find_packages


setup(
    name="ibdp_classes",
    version="0.1.2",
    description="A basic implementation of the restrictive classes that may be used in IBDP Computer Science exams",
    long_description=(pathlib.Path(__file__).parent / "readme.md").read_text(),
    long_description_content_type="text/markdown",
    author="Richard Ambler",
    license="MIT Licence",
    author_email="rambler@wya.top",
    url="https://github.com/ram6ler/ibdp_classes",
    install_requires=[],
    packages=find_packages(),
)
