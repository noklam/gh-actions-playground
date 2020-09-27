import re
from setuptools import setup, find_packages

with open("gh_actions_playground/__init__.py", encoding="utf-8") as file_handler:
    version = re.search(r'__version__ *= *["\']([^"\']+)', file_handler.read()).group(1)

setup(
    name='gh_actions_playground',
    version=version,
    author='Author Name',
    author_email='author@gmail.com',
    description='Tests for CI',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1'],
)