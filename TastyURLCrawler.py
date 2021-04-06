# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import json
from bs4 import BeautifulSoup
import urllib
import ast

class TASTYURLCrawler:
    """
    Tasty URL Crawler
    Generate the list the url links to start with, from Tasty Website
    """
    def __init__(self):
        self.out = {}

    def getSoup(self, url):
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "lxml")
        return soup

    def getJSON(self, url):
        soup = self.getSoup(url)
        
        link_pool = []
        for aurl in soup.find_all('a'):
            if aurl.get('class')[0] == "feed-item":
                url = aurl.get("href")
                if url[1:7] == "recipe":
                    link_pool.append(url)
            
        self.link_pool = link_pool

        return self.link_pool
