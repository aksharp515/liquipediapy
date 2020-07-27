import liquipediapy.exceptions as ex
from liquipediapy.liquipediapy import liquipediapy
import re
from liquipediapy.rocketleague_modules.match import rl_match
from liquipediapy.rocketleague_modules.tournament import rl_tournament
from liquipediapy.rocketleague_modules.top_team import rl_top_team
import unicodedata
import time

class rocketleague():

    def __init__(self,appname):
        self.appname = 'Rocket League Alert'
        self.liquipedia = liquipediapy(appname,'rocketleague')
        self.__image_base_url = 'https://liquipedia.net'

    def get_matches(self):
        rl_match_object = rl_match()
        matches = []
        soup,__ = self.liquipedia.parse('Liquipedia:Matches')		
        time_local = time.mktime(time.localtime())
        for table_content in soup.find_all('div'):
            if table_content.attrs.get('data-toggle-area-content') == '1':
                for match_content in table_content.find_all('table', class_='infobox_matches_content'):
                    match = {}
                    match['team-left'] = rl_match_object.get_team_in_match('team-left', match_content)
                    match['team-right'] = rl_match_object.get_team_in_match('team-right', match_content)
                    match['time'] = int(rl_match_object.get_time(match_content))
                    time_match = time.mktime(time.localtime(match['time']))
                    match['timetill'] = round((time_match - time_local) / 60)
                    match['tournament_name'] = rl_match_object.get_match_tournament_name(match_content)
                    match['tournament_wiki_link'] = rl_match_object.get_match_tournament_wiki_link(match_content)
                    matches.append(match)
                return matches
                            
    def get_recent_tournaments(self):
        tournaments = []
        rl_tournament_object = rl_tournament()
        soup,__ = self.liquipedia.parse('Portal:Tournaments')		
        tournaments_div = soup.find(id="Three_Most_Recent").parent.next_sibling.next_sibling
        for tournament_content in tournaments_div.find_all('div', class_='divRow'):
            tournament = {}
            tournament['name'] = rl_tournament_object.get_tournament_name(tournament_content)
            tournament['date'] = rl_tournament_object.get_tournament_date(tournament_content)
            tournament['link'] = rl_tournament_object.get_tournament_link(tournament_content)
            tournament_soup,__ = self.liquipedia.parse(str(tournament['link'].replace('/rocketleague/','')))
            tournament['twitch_link'] = rl_tournament_object.get_tournament_twitch_link(tournament_soup)
            tournaments.append(tournament)
        return tournaments


    def get_top_teams(self, teams_of_interest=16):
        rl_top_team_object = rl_top_team()
        top_teams = []
        soup,__ = self.liquipedia.parse('Portal:Rating')		
        count = 0
        for team in soup.find_all('span', class_='team-template-team-standard'):
            count+=1
            top_teams.append(rl_top_team_object.get_top_team(team))
            if (count >= teams_of_interest):
                break
        return top_teams

