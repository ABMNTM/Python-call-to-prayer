from time import sleep
from datetime import datetime
import os
import requests
import re
from bs4 import BeautifulSoup
def totime(n):
    min = int(n[3:])
    hour = int(n[:2])
    min += 30
    if min >= 60:
        min -= 60
        hour += 1
    hour += 3
    if hour < 10:
        hour = '0' + str(hour)
    if min < 10:
        min = '0' + str(min)
    return str(hour) + ':' + str(min)
res = requests.get('https://badesaba.ir/owghat/1184/%D9%87%D9%85%D8%AF%D8%A7%D9%86')
if res.status_code == 200:
    print("operation done!")
    soup = BeautifulSoup(res.text, 'html.parser')
    all_times = soup.find_all('p', attrs={'class': 'time'})
    li_times = []
    for time in all_times:
        li_times.append(str(re.sub(r'<p _ngcontent-sc88="" class="time"> 'and r' </p>','', time.text)).strip())
    table = '-' * 21
    azan = ['Sobhh','tolu`', 'zohhrr', 'aasrr','qorub' , 'maqreb', 'ei`sa', 'nimeh']
    print(f'+ {table} +')
    for i in range(len(azan)):
        print(f'|  {azan[i]}\t{li_times[i]}   |')
    print(f'+ {table} +')
    
    while True:
        time = (str(datetime.now()).split('-'))[2][3:8]
        for t in li_times:
            if time == t:
                azan = "Azan.mp3"
                os.system("mpg123 " + azan)
else:
    print("cannot scrape from 'badesaba'\n\ntry to do it from another way . . . ")