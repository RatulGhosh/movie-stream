
"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(name="tvlc",
	  version="0.5",
	  description="Stream movies directly from torrent",
	  url="https://github.com/RatulGhosh/movie-stream",
	  author="Ratul Ghosh",
	  author_email="ratulghoshr@gmail.com",
	  license='MIT',
	  packages=["tvlc"],
	  scripts=["bin/tvlc.py"],
	  long_description=open('README.rst').read(),
	  install_requires=[
		  'BeautifulSoup4',
		  'requests'],
)
