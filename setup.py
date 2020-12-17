from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Given recent trades and order books from a set of trading venues, predict on which trading venue the next trade will be executed.',
    author='pyrrho',
    license='MIT',
)
