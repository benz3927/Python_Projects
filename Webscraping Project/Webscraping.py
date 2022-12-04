# ideas scraping for NBA or tennis player data, economics Fed interest rates, etc. something else

from bs4 import BeautifulSoup
import requests

    
def link_getter(movie,parsed_code):
    everything = parsed_code.find_all("h3", class_ = "lister-item-header")

    for title in everything:
        a = title.find("a")
        if a.text == movie:
            movie_url = "https://www.imdb.com" + a["href"]
            return movie_url
    

# def get_cast(movie_url,parsed_code):
#     cast_url = movie_url + "fullcredits/?ref_=tt_cl_sm"
#     cast_source_code = requests.get(cast_url).text
#     cast_parsed_code = BeautifulSoup(cast_source_code, "html.parser")
    

# tr, td, then a
# table cast list, td, tr, a
#     layer1 = parsed_code.find_all("td", class_ = "character")
#     print(layer1)
#     layer2 = layer1[0].find_all("td", class_ = "lister-item-header")
#     for index in layer2:
#         a = parsed_code.find("a", class_ = "lister-item-header")
#     return a
    

        
def main():
    url = "https://www.tennisexplorer.com/ranking/atp-men/"
    source_code = requests.get(url).text
    parsed_code = BeautifulSoup(source_code, "html.parser")
    
    everything = parsed_code.find_all("table", class_ = "result")


#     print(everything[1])
    
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

        
        
    
    
#     for index in range(len(chunk)):
#         if (chunk[index].text == "t-name"):
#             print(chunk[index + 1].text) 
    
    
    
    #     print(everything)

#     player = everything.find("thead")
    
#     for item in everything:
#         print(item.find("thead"))

#         print(item.find("t-name").text)
    
#     everything = parsed_code.find_all("a href", class_ = "lister-item-header")

#     for title in everything:
#         print(title.find("a").text)
    
#     movie = input('give me a movie name: ')
#     movie_url = link_getter(movie,parsed_code)
#     print(movie_url)
#     
#     print(get_cast(movie_url,parsed_code))
    


main()

