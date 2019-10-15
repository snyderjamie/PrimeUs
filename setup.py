from setuptools import setup, find_packages

setup(
    name='PrimeUs',
    description='A practical prime problem programmed in Python',
    author='Andrew Wyllie',
    author_email='wyllie@dilex.net',
    version='1.0.0',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    license='MIT License',
    long_description=open('README.md').read()
)
