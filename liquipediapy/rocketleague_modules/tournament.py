import re
from urllib.request import quote
import unicodedata

class rl_tournament():
    def get_tournament_name(self,tournament_content):
        for tournament in tournament_content.find_all('div', class_='divCell Tournament Header'):
            return (tournament.b.a.text)

						
    def get_tournament_date(self,tournament_content):
        for tournament_date in tournament_content.find_all('div', class_='divCell EventDetails Date Header'):
            return tournament_date.text

    def get_tournament_link(self,tournament_content):
        for tournament in tournament_content.find_all('div', class_='divCell Tournament Header'):
            return (tournament.b.a['href'])

    def get_tournament_twitch_link(self, tournament_soup):
        tournament_divs = tournament_soup.find_all('div')
        for div in tournament_divs:
            if (div.text == 'Links'):
                for atag in div.parent.next_sibling.next_sibling.find_all('a'):
                    if (atag['href'].find('twitch') != -1):
                        return atag['href']
