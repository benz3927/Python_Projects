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
    print(countries)
    
    player_country = {}
    for country in countries:
        player_country[country] = 0
    
    for item in chunk:
        item = item.text
        item = item.split("\n")
        if item[4][2:] in player_country:
            player_country[item[4][2:]] += 1
            
    return player_country

        
def main():
    print(country_counter('https://www.tennisexplorer.com/ranking/atp-men/?page=1)'))
    
    countries = ('Spain', 'Norway', 'Greece', 'Serbia', 'Canada', 'Russia', 'USA', 'Poland', 'Denmark', 'Germany', 'Great Britain', 'Italy', 'Croatia', 'Australia', 'Argentina', 'Bulgaria', 'Netherlands', 'Japan', 'Kazakhstan', 'Finland', 'France', 'Slovakia')
    y_pos = np.arange(len(countries))
    performance = [6,1,1,2,2,3,9,1,1,1,4,4,2,2,3,1,1,1,1,1,2,1]
# 
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, countries)
    plt.ylabel('Players')
    plt.title('Countries in the Top 50')
    
    plt.show()

    
main()

