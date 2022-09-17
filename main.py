from pprint import pprint
import requests
import time
from datetime import date, timedelta, datetime

today = date.today() 
today_2 = today - timedelta(days=2)
today_unix =  int(time.mktime(time.strptime(str(today), '%Y-%m-%d')))
today_unix_2 =  int(time.mktime(time.strptime(str(today_2), '%Y-%m-%d')))


url = 'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow'
params = {
    #'page': 1,
    #'pagesize': 2,
    'fromdate': today_unix_2,
    'max': today_unix
}
res = requests.get(url, params)
sample = res.json()
#pprint(sample)

result = []
for s1 in sample['items']:
    for s2 in s1['tags']:
        if s2.lower() == 'python':
            result.append(s1['title'])
pprint(result)

print(f'Все вопросы с {today_2} по {today}')