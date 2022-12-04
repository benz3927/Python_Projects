"""
Prompt: Scrape that website for the Argentinian goalkeepers
Output should be:
Franco Armani
Emiliano Martinez
Geronimo Rulli

"""
import requests
from bs4 import BeautifulSoup

def main():
    URL = "https://www.sportingnews.com/us/soccer/news/world-cup-squads-2022-team-rosters-official-fifa-qatar/kjcagctfesjt0zpjxctbdqha"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    argentina = soup.find("table")
    argentina_players = argentina.find_all("td")
    for index in range(len(argentina_players)):
        if (argentina_players[index].text == "Goalkeeper"):
            print(argentina_players[index + 1].text)
main()
    
    