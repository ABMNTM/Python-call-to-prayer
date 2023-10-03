##  ## ## ## ## ## ## ## ## ##  ##
#                                #
#   this is a simple logic for   #
#    calling to prayer 'azan'    #
#                                #
##  ## ## ## ## ## ## ## ## ##  ##

from time import sleep
from datetime import datetime
from pydub import AudioSegment
from pydub.playback import play
import requests
import re
from bs4 import BeautifulSoup

def table(times:list) -> None : # to printing an 'azan' table
    table = '-' * 21
    azan = ['Sobhh','tolu`', 'zohhrr', 'aasrr','qorub' , 'maqreb', 'ei`sa', 'nimeh']
    print(f'+ {table} +')
    for i in range(len(azan)):
        print(f'|  {azan[i]}\t{times[i]}   |')
    print(f'+ {table} +')


# scrapping from 'badesaba' (an iranian islamic calendar with intersting features =))

res = requests.get('https://badesaba.ir/owghat/1184/%D9%87%D9%85%D8%AF%D8%A7%D9%86')


# if scrapping done successfully

if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    ini_times = soup.find_all('p', attrs={'class': 'time'}) # getting all azan times
    main_times = []  # for storing trimmed azan times
    for time in ini_times:
        # trimming initial azan times
        main_times.append(str(re.sub(r'<p _ngcontent-sc88="" class="time"> 'and r' </p>','', time.text)).strip())

    table(main_times)

    while True:
        sleep(.5)
        # checking the current time to identify azan time
        time = (str(datetime.now()).split('-'))[2][3:8]
        for t in main_times:
            if time == t:
                song = AudioSegment.from_mp3("Azan.mp3")
                play(song)        
else:
    print("cannot scrape from 'badesaba'")

# thank you for your attention and spending time #