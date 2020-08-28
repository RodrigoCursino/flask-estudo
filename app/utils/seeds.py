import requests
import json
import requests
from   bs4 import BeautifulSoup

class Seed():

    __leagues = ['ENG', 'ESP', 'BRA', 'FRA', 'GER', 'ITA', 'CHN', 'POR','ARG', 'JPN', 'CHI', 'URU', 'PAR', 'BOL', 'PER', 'COL', 'MEX']

    def __init__(self, countries=[]):
        self.countries  = countries

    def get_teams(self):
        for country in self.countries:
            print(country)
            if (country in self.__leagues):
                for division in range(1,4):
                    
                    print(f"Obtendo dados da liga {country}")
                    
                    response = requests.get(f'https://site.web.api.espn.com/apis/site/v2/sports/soccer/{country}.{division}/teams?region=br&lang=pt&contentorigin=deportes&limit=400&includeModules=news').json()

                    print("Lendo ...")

                    if('sports' in response):
                        for sport in response['sports']:
                            for leagues in sport['leagues']:
                                for team in leagues['teams']:
                                    self._save_team(team, country)    
                        
                    print(f"Finalizando divisão {division}")
   
    """
     Faz um scraping na tela para buscar jogadores por time
     :param: link type string:
     :param: team type Team:
    """
    def _get_players(self, squad, team):
        
        re   = requests.get(squad)
        soup = BeautifulSoup(re.text, 'lxml')

        content = soup.find("div", class_ = "Card__Content") 
        
        if(content):
            # for table in tables:
            for tables in content.find_all('table'):
                for table in tables.find_all('tbody'):
                    rows = table.find_all('tr')
                
                    for row in rows:
                        cols = row.find_all('td')
                        for col in cols:
                            span = cols[0].find("span", class_="n10")
                            camisa = ""
                            if(span):
                                camisa = span.text

                            height = None
                            if(cols[3].text[0:4] != '--'):
                                height = float(cols[3].text[0:4])
                            
                            weight = None
                            if(cols[4].text[0:3] != '--'):
                                weight = int(cols[4].text[0:3])
                            player = {
                                'team_id': team,
                                'player_number': camisa,
                                'name': cols[0].a.text,
                                'position': cols[1].text,
                                'height': height,
                                'weight': weight,
                                'country': cols[5].text,
                                "picture": "",
                                "feature": "",
                                "default_leg": "",
                                "birth_date": "",
                                "date_begin": "",
                                "date_end": ""
                            }
                            self._save_players(player)
                            break

    """
    Sava um time
    :param: pais type string:
    :param: team type Team:
    """
    def _save_team(self, team, country):
 
        link           = team['team']['links'][5]['href']
        color          = ""
        alternateColor = ""
        logo           = ""

        if ('color' in team['team']):
            color = team['team']['color']
        
        if ('alternateColor' in team['team']):
            alternateColor = team['team']['alternateColor']

        if ('logos' in team['team']):
            logo = team['team']['logos'][0]['href']

        payload = {
                "name"               : team['team']['name'],
                "country"            : country,
                "brand"              : logo,
                "color"              : color,
                "alternateColor"     : alternateColor,
                "abbreviation"       : team['team']['abbreviation'],
                "uniform_one"        : "",
                "uniform_two"        : "",
                "foundation_date"    : "", 
        }
        
        headers = {'content-type': 'application/json'}
        save  = requests.post('http://localhost:5000/teams/', data = json.dumps(payload), headers = headers)
        
        response = save.json()
        print(response)
        self._get_players(link, response['team'])

    """
    Sava um Jogador
    :param: player type Player:
    """
    def _save_players(self, player):
            
        headers = {'content-type': 'application/json'}
        save  = requests.post('http://localhost:5000/players/', data = json.dumps(player), headers = headers)
        
        print("jogador ", save)
    