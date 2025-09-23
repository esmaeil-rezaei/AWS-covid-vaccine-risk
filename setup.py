from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> list[str]:
    """
    This function reads a requirements file and returns a list of required packages.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Remove comments and empty lines
    requirements = [line.strip() for line in lines if line.strip() and not line.startswith('#')]

    if '-e .' in requirements:
        requirements.remove('-e .')
    
    return requirements

setup(
    name='Covid Vaccine Heart Attack Risk Analysis',
    version='0.0.1',
    author='Ishmael',
    author_email='ishmaelrezaei@gmail.com',
    description='A package to analyze the heart attack risk of COVID-19 vaccines',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)