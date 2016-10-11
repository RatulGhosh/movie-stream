#!/usr/bin/env python

import os
import sys
import requests
from bs4 import BeautifulSoup


def get_movie():
    """Gets the movie name from user and formats it."""

    try:
        movie_name = raw_input("Enter movie name : ")
        query = (movie_name).replace(' ', '%20')+'/'
    except Exception as e:
        print e
        exit()
    return query


def stream_movie(search_url):
    """Finds the torrent having the maximum seed."""
	
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
    #print 'peerflix ' + '\"' + link1 + '\"' + ' --vlc'

    os.system('peerflix ' + '\"' + link1 + '\"' + ' --vlc')    


if __name__ == "__main__":

    movie = get_movie()
    url = 'http://www.yify-movies.net/search/' + movie + 'seed/'
    try:
        print 'Searching....'
        stream_movie(url)
    except Exception as e:
        print e
        exit()
