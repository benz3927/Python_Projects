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
        
        # the 4th indexed value in item is the tennis player's country
        if item[4][2:] not in countries:
            countries.append(item[4][2:])

    
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
# Scraping 2022 Data
    year2022 = "https://www.tennisexplorer.com/ranking/atp-men/2022/"
    year2022_dict = country_counter(year2022)
    
    # sorted takes a dictionary and makes it a list of tuples. Sorts the values of the counts within the lists
    
    year2022_sorted = sorted(year2022_dict.items(), key=lambda x:x[1], reverse = True)
    
    # We take our sorted list of tuples and make it back into a dictionary
    year2022_dict = dict(year2022_sorted)
    
    # extract the scores (country) and keys (counts of top 100 ATP-ranked tennis player) for use in graphing
    countries2022 = list(year2022_dict.keys())
    player_counts2022 = np.sort(list(year2022_dict.values()))[::-1]
    


# Scraping 2014 Data
    year2014 = "https://www.tennisexplorer.com/ranking/atp-men/2014/"
    year2014_dict = country_counter(year2014)
    
    # sorted takes a dictionary and makes it a list of tuples. Sorts the values of the counts within the lists
    
    year2014_sorted = sorted(year2014_dict.items(), key=lambda x:x[1], reverse = True)
    
    # We take our sorted list of tuples and make it back into a dictionary
    year2014_dict = dict(year2014_sorted)
    
    # extract the scores (country) and keys (counts of top 100 ATP-ranked tennis player) for use in graphing
    countries2014 = list(year2014_dict.keys())
    player_counts2014 = np.sort(list(year2014_dict.values()))[::-1]
    
    
# Scraping 2009 Data
    year2009 = "https://www.tennisexplorer.com/ranking/atp-men/2009/"
    year2009_dict = country_counter(year2009)
    
    # sorted takes a dictionary and makes it a list of tuples. Sorts the values of the counts within the lists
    
    year2009_sorted = sorted(year2009_dict.items(), key=lambda x:x[1], reverse = True)
    
    # We take our sorted list of tuples and make it back into a dictionary
    year2009_dict = dict(year2009_sorted)
    
    # extract the scores (country) and keys (counts of top 100 ATP-ranked tennis player) for use in graphing
    countries2009 = list(year2009_dict.keys())
    player_counts2009 = np.sort(list(year2009_dict.values()))[::-1]

# Scraping 2005 Data
    year2005 = "https://www.tennisexplorer.com/ranking/atp-men/2005/"
    year2005_dict = country_counter(year2005)
    
    # sorted takes a dictionary and makes it a list of tuples. Sorts the values of the counts within the lists
    
    year2005_sorted = sorted(year2005_dict.items(), key=lambda x:x[1], reverse = True)
    
    # We take our sorted list of tuples and make it back into a dictionary
    year2005_dict = dict(year2005_sorted)
    
    # extract the scores (country) and keys (counts of top 100 ATP-ranked tennis player) for use in graphing
    countries2005 = list(year2005_dict.keys())
    player_counts2005 = np.sort(list(year2005_dict.values()))[::-1]
    
    
# Scraping 2000 Data
    year2000 = "https://www.tennisexplorer.com/ranking/atp-men/2000/"
    year2000_dict = country_counter(year2000)
    
    # sorted takes a dictionary and makes it a list of tuples. Sorts the values of the counts within the lists
    
    year2000_sorted = sorted(year2000_dict.items(), key=lambda x:x[1], reverse = True)
    
    # We take our sorted list of tuples and make it back into a dictionary
    year2000_dict = dict(year2000_sorted)
    
    # extract the scores (country) and keys (counts of top 100 ATP-ranked tennis player) for use in graphing
    countries2000 = list(year2000_dict.keys())
    player_counts2000 = np.sort(list(year2000_dict.values()))[::-1]
    

    
    
    # DPI = 1200 is used to improve/increase the resolution of matplotlib
    # plt.figure(figsize=(8, 8)) is used to increase size of image
    
    # Graph Matplotlib Barplots
    
    #2000
    plt.figure(figsize=(8, 8))
    plt.bar(countries2000, player_counts2000, align='center', alpha=0.5)
    plt.xticks(rotation=60, ha='right', fontsize = 6.5)
    plt.ylabel('Country')
    plt.title('Top 100 ATP Tennis Players by Country in 2000')
    plt.savefig("2000 Tennis Players by Country.png", format="png", dpi=1200)
    plt.show()

    
    #2005
    plt.figure(figsize=(8, 8))
    plt.bar(countries2005, player_counts2005, align='center', alpha=0.5)
    plt.xticks(rotation=60, ha='right', fontsize = 6.5)
    plt.ylabel('Country')
    plt.title('Top 100 ATP Tennis Players by Country in 2005')
    plt.savefig("2005 Tennis Players by Country.png", format="png", dpi=1200)
    plt.show()
    
    #2009
    plt.figure(figsize=(8, 8))
    plt.bar(countries2009, player_counts2009, align='center', alpha=0.5)
    plt.xticks(rotation=60, ha='right', fontsize = 6.5)
    plt.ylabel('Country')
    plt.title('Top 100 ATP Tennis Players by Country in 2009')
    plt.savefig("2009 Tennis Players by Country.png", format="png", dpi=1200)
    plt.show()
    
    #2014
    plt.figure(figsize=(8, 8))
    plt.bar(countries2014, player_counts2014, align='center', alpha=0.5)
    plt.xticks(rotation=60, ha='right', fontsize = 6.5)
    plt.ylabel('Country')
    plt.title('Top 100 ATP Tennis Players by Country in 2014')
    plt.savefig("2014 Tennis Players by Country.png", format="png", dpi=1200)
    plt.show()
    
    
    #2022
    plt.figure(figsize=(8, 8))
    plt.bar(countries2022, player_counts2022, align='center', alpha=0.5)
    plt.xticks(rotation=60, ha='right', fontsize = 6.5)
    plt.ylabel('Country')
    plt.title('Top 100 ATP Tennis Players by Country by Country in 2022')
    plt.savefig("2022 Tennis Players by Country.png", format="png", dpi=1200)
    plt.show()
    

    
main()

