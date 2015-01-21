import json
from pprint import pprint
import datetime
import sys

laskuri = {}

a = ["Vaalit", "miten", "Suomen", "Miten"]
b = ["Vihree", "Punainen", "Sininen"]
c = ["odottaa", "alkaa", "moi"]

kaikki_teemat = [a, b, c]

teema1 = {}

isoteema = len(kaikki_teemat)

for tiedosto in sys.argv[1:]:

    with open(tiedosto) as json_data:
        d = json.load(json_data)
        json_data.close()

        for tweet in d:
            aika = datetime.datetime.fromtimestamp(
                    int(tweet['time'])
                ).strftime('%Y-%m-%d')

            if aika not in laskuri:
                laskuri[aika] = 0

            laskuri[aika] += 1

            teema_lista = tweet['text']

            if aika not in teema1:
                teema1[aika] = 0

            for y in range(0, isoteema):
        
                flag = False
                for x in kaikki_teemat[y]:
                    if x in teema_lista and flag == False:
                        teema1[aika] += 1
                        flag = True
                
        ##print teema_lista
#print teema1
#print teema2
#print teema3

    for paiva in sorted( laskuri.keys()):
        print paiva , "," , laskuri[ paiva ], "," , teema1[paiva]






