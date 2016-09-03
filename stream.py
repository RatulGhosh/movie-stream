#!/usr/bin/env python

import os
import sys
import requests
from bs4 import BeautifulSoup


def test_system():
    """Runs few tests to check if npm and peerflix is installed on the system."""
    if os.system('npm --version') != 0:
        print 'NPM not installed installed, please read the Readme file for more information.'
        exit()
    if os.system('peerflix --version') != 0:
        print 'Peerflix not installed, installing..'
        os.system('npm install -g peerflix')


def get_movie():
    """Gets the input from user and formats it."""
    try:
        movie_name = raw_input("Enter movie name : ")
        query = (movie_name).replace(' ', '%20')+'/'
    except Exception as e:
        print e
        exit()
    return query


def stream_movie(search_url):
    """Grabs the best matched torrent URL from the search results."""
	
    #print search_url
    search_request_response = requests.get(search_url, verify=False)
    soup = BeautifulSoup(search_request_response.text, 'html.parser')
    letters = soup.find_all("div", class_="download-movies")
    link = letters[0].a["href"]
    link = 'http://www.yify-movies.net'+link

    search_request_response = requests.get(link, verify=False)
    soup = BeautifulSoup(search_request_response.text, 'html.parser')
    letters = soup.find_all("div", class_="wish-list")
    link1 = letters[0].a["href"]
    print 'peerflix ' + '\"' + link1 + '\"' + ' --vlc'

    #os.system('peerflix ' + '\"' + link1 + '\"' + ' --vlc')    

    """movie_page = 'http://www.yify-movies.net' + (soup.find_all("a", class_="cellMainLink")[0].get('href'))

    search_url = requests.get(movie_page, verify=False)
    soup = BeautifulSoup(search_url.text, 'html.parser')
    torrent_url = 'http:' + soup.find_all('a', class_='siteButton')[0].get('href')
    return torrent_url"""

if __name__ == "__main__":
    #test_system()
    movie = get_movie()
    url = 'http://www.yify-movies.net/search/' + movie + 'seed/'
    stream = ''
    try:
        print 'Searching....'
        stream = stream_movie(url)
    except Exception as e:
        print e
        exit()
