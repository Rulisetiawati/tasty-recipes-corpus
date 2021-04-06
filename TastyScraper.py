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
import re
import requests
# #!pip install Unidecode
from unidecode import unidecode


class TASTYScraper:
    """
    Tasty Scraper
    Scrapes recipe and other content from Tasty Website
    """
    def __init__(self):
        self.out = {}

    def getSoup(self, url):
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "lxml")
        return soup

    def getJSON(self, url):
        
        soup = self.getSoup(url)
        
        # Title
        if soup.find("h1", {"class": "recipe-name extra-bold xs-mb05 md-mb1"}):
            self.out["title"] = soup.find("h1", {"class": "recipe-name extra-bold xs-mb05 md-mb1"}).text
            content_json = json.loads("".join(soup.find("script", {"type":"application/ld+json"}).contents))

            # Ingredients section
            self.out["ingredients"] = [unidecode(content) for content in content_json.get("recipeIngredient", "")]

            # Preparation section
            preparation = [ing.get("text", "") for ing in content_json["recipeInstructions"]]
            self.out["preparation"] = preparation

            # Description
            self.out["description"] = content_json.get("description", "")

            # Reciepe yield
            #self.out["reciepe_yield"] = content_json.get("recipeYield", "")

            # Cooking Method
            #self.out["cookingMethod"] = content_json.get("cookingMethod", "")

            # Tools
            #self.out["tool"] = content_json.get("tool", "")

            # Get related recipe links
            # get meta_id
            for meta in soup.find_all('div'):
                if meta.get("data-recipe-id"):
                    meta_id = meta.get("data-recipe-id")

            api_link = "https://tasty.co/api/proxy/tasty/recipe/" + meta_id + "/related"
            api_json = requests.get(api_link).json()

            slug_list = []
            for item in api_json['items']:
                slug_list.append(item['slug'])

            related_links = []

            for slug in slug_list:
                related_recipe_link = "https://tasty.co/recipe/" + slug
                related_links.append(related_recipe_link)
        
            self.out['relatedRecipes'] = related_links
        
        return self.out
