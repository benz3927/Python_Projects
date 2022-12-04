# ideas scraping for NBA or tennis player data, economics Fed interest rates, etc. something else

from bs4 import BeautifulSoup
import requests
import numpy as np
import matplotlib.pyplot as plt

def country_counter(url):
    source_code = requests.get(url).text
    parsed_code = BeautifulSoup(source_code, "html.parser")
    
    everything = parsed_code.find_all("table", class_ = "result")
    
    chunk = everything[1].find_all("tr")
    countries = []
    
    for item in chunk:
        item = item.text
        item = item.split("\n")
        
        # the 5th indexed value is country
        if item[4][2:] not in countries:
            countries.append(item[4][2:])
    countries = countries[1:]
    
    player_country = {}
    for country in countries:
        player_country[country] = 0
    
    for item in chunk:
        item = item.text
        item = item.split("\n")
        if item[4][2:] in player_country:
            player_country[item[4][2:]] += 1
            
    url2  = url + '?page=2'
    
    ## repeat process for url 2
    
    
    source_code = requests.get(url2).text
    parsed_code = BeautifulSoup(source_code, "html.parser")
    
    everything = parsed_code.find_all("table", class_ = "result")
    
    new_chunk = everything[1].find_all("tr")
    
    for item in new_chunk:
        item = item.text
        item = item.split("\n")
        
        # the 5th indexed value is country
        if item[4][2:] not in countries:
            countries.append(item[4][2:])
    
    countries = countries[1:]
    countries.remove('ountry')
    for country in countries:
        if country not in player_country:
            player_country[country] = 0
    
    for item in new_chunk:
        item = item.text
        item = item.split("\n")
        if item[4][2:] in player_country:
            player_country[item[4][2:]] += 1
    
    
            
    return player_country

        
def main():

    url = "https://www.tennisexplorer.com/ranking/atp-men/"
    print(country_counter(url))
    
main()

