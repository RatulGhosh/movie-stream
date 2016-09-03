
from setuptools import setup

setup(name="tms",
	  version="2.7",
	  description="Stream movies directly from torrent",
	  url="https://github.com/RatulGhosh/movie-stream",
	  author="Ratul Ghosh",
	  author_email="ratulghoshr@gmail.com",
	  license='MIT',
	  packages=["tms"],
	  scripts=["bin/tms"],
	  install_requires=[
		  'BeautifulSoup4',
		  'requests'],
	  zip_safe=False)
