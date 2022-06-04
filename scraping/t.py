import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

page = requests.get('https://m6competition.com/Leaderboard')
soup = BeautifulSoup(page.content, parser='lxml')

quarter = soup.find('select', {'id': 'selectQuarter'})
quarter_ids = [(i['value'], i.get_text()) for i in quarter.find_all('option')]

month = soup.find('select', {'id': 'selectCompetition'})
month_ids = [(i['value'], i.get_text()) for i in month.find_all('option')]

urls = {
    'Quarter': quarter_ids,
    'Competition': month_ids,
    'Global': [('', '')],
}

for period, ids in urls.items():
    for competitionid, name in ids:
        page = requests.get(f'https://m6competition.com/Leaderboard/PeriodData?period={period}&competitionId={competitionid}')
        content = json.loads(page.content)
        today = pd.Timestamp.now().strftime('%Y-%m-%d')
        df = pd.DataFrame(content['data'])
        df.to_csv(f'{period}_{name}_{today}.csv')

