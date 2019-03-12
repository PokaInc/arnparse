from distutils.core import setup
import setuptools  # required for running `python setup.py bdist_wheel`

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='arnparse',
    packages=['arnparse'],  # this must be the same as the name above
    version='0.0.2',
    description='Parse ARNs using Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Simon-Pierre Gingras',
    author_email='spgingras@poka.io',
    url='https://github.com/PokaInc/arnparse',  # use the URL to the github repo
    download_url='https://github.com/PokaInc/arnparse/tarball/0.0.1',
    keywords=['aws', 'arn', 'parse'],  # arbitrary keywords
    install_requires=[],
    classifiers=[],
)
