from setuptools import find_packages,setup

setup(
    name = 'mlproject',
    version='0.0.1',
    author='Rushikesh',
    author_email='rushikeshsk2105@gmail.com',
    packages = find_packages(),
    install_requires = ['pandas','numpy','seaborn']
)