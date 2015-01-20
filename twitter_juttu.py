import json
from pprint import pprint
import datetime
import sys

laskuri = {}

a = ["Vaalit", "miten", "Suomen", "Miten"]
b = ["Vihree", "Punainen", "Sininen"]
c = ["odottaa", "alkaa", "moi"]

teema1 = {}
teema2 = {}
teema3 = {}

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

            if aika not in teema2:
                teema2[aika] = 0

            if aika not in teema3:
                teema3[aika] = 0

            for x in a:
                if x in teema_lista:
                    teema1[aika] += 1
                
            for x in b:
                if x in teema_lista:
                    teema2[aika] += 1
                
            for x in c:
                if x in teema_lista:
                    teema3[aika] += 1

        ##print teema_lista
#print teema1
#print teema2
#print teema3

    for paiva in sorted( laskuri.keys()):
        print paiva , "," , laskuri[ paiva ], "," , teema1[paiva], ",", teema2[paiva], ",", teema3[paiva]






