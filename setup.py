from distutils.core import setup
from setuptools import find_packages
from glob import glob

setup(
    name='roboverse',
    packages=find_packages(),
    include_package_data=True,
    data_files = [
        ('assets', glob('roboverse/roboverse/assets/**/*.py', recursive=True))
    ],
)
