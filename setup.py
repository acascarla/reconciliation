from setuptools import setup
from setuptools import find_packages

__version__ = '0.0.1'

setup(
    name='oalfonso-reconciliation',
    version=__version__,
    long_description='Importing and reconciling from CSV + API View',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django<=3.0',
        'psycopg2-binary<=2.9',
        'python-dotenv==0.10.2',
        'djangorestframework<=3.10',
    ],
)
