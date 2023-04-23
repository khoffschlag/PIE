from setuptools import setup, find_packages

setup(
    name='PIE',
    version='0.1',
    author='Kevin Hoffschlag',
    description='PIE is a Python module that allows you to plot inequalities and equations as well as the intersections between them.',
    packages=find_packages(),
    install_requires=['jupyterlab', 'numpy', 'matplotlib'],
)
