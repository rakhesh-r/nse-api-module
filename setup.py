from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name='nse-api-module',
    version='0.1.0',
    description='Module which gives data from nse website',
    long_description=readme,
    author='Rakhesh R',
    author_email='rksh77@gmail.com',
    url='https://github.com/rakhesh-r/nse-api-module',
    packages=find_packages(exclude='tests')
)