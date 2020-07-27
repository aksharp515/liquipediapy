import re
from urllib.request import quote
import unicodedata

class rl_top_team():
    def get_top_team(self, team):
        spans = team.find_all('span', class_= 'team-template-text')
        retval = ""
        for top_team in spans[0].find_all('a'):
             retval = top_team.get('title')

        return retval
