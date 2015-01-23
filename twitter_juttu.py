import json
from pprint import pprint
import datetime
import sys

laskuri = {}

a = ["Vaalit", "miten", "Suomen", "Miten"]
b = ["tavoittelu", "kiva", "Sininen"]
c = ["odottaa", "on", "moi"]

kaikki_teemat = [a, b, c]

isoteema = len(kaikki_teemat)

laskuri_teemat = []

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
        
            for y in range(0, isoteema):

                laskuri_teemat.append({}) 

                if aika not in laskuri_teemat[y]:
                    laskuri_teemat[y][aika] = 0

            
                flag = False
                for x in kaikki_teemat[y]:
                    if x in teema_lista and flag == False:
                        laskuri_teemat[y][aika] += 1
                        flag = True

    for paiva in sorted( laskuri.keys()):
        print paiva , "," , laskuri[ paiva ], "," , laskuri_teemat[0][paiva], "," , laskuri_teemat[1][paiva], "," , laskuri_teemat[2][paiva]
