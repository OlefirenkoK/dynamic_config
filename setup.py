import os

from setuptools import setup, find_packages


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


setup(
    name='dynamo',
    version='0.1',
    author='Olefirenko K',
    description='',
    install_requires=read('requirements.txt'),
    packages=find_packages(),
    include_package_data=True,
)
