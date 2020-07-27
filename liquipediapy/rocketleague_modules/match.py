import re
from urllib.request import quote
import unicodedata

class rl_match():
    def get_team_in_match(self, team, match_content):
        data = match_content.find_all('td', class_= team)
        retval = ""
        for dataVal in data[0].find_all('span', class_='team-template-text'):
            for aTag in dataVal.find_all('a'):
                 retval = (aTag.get('title'))

        #cleanup names before sending back
        if retval == "": 
            retval = "TBD"
        else:
            dne = retval.find("(page")
            if dne != -1:
                retval = retval[:dne-1]

        return retval

    def get_time(self, match_content):
        data = match_content.find_all('span', class_= 'match-countdown')
        for dataVal in data[0].find_all('span'):
             return (dataVal.get('data-timestamp'))

    def get_match_tournament_name(self, match_content):
        data = match_content.find_all('td', class_= 'match-filler')
        for dataVal in data[0].find_all('a'):
            return dataVal['title']

    def get_match_tournament_wiki_link(self, match_content):
        data = match_content.find_all('td', class_= 'match-filler')
        for dataVal in data[0].find_all('a'):
            return dataVal['href']
