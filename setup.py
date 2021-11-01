from distutils.core import setup
from setuptools import find_packages
import glob

setup(
    name='roboverse',
    packages=find_packages(),
    include_package_data=True,
    data_files = [
        glob('roboverse/roboverse/assets/*')
    ],
)
