from setuptools import find_packages,setup
from typing import List



setup(
    name='DimondPricePrediction',
    version='0.0.1',
    author='Vansh',
    author_email='vansh.malhotra@seaflux.tech',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)