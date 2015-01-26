import json
from pprint import pprint
import datetime
import sys

laskuri = {}

teemat = "teemat.txt"

tiedosto = open(teemat, 'r')

jako = []

for line in tiedosto:
    line = line.strip()
    jako.append(line.split(","))

teema_lasku = len(jako)

teemat_lista = []

for tiedosto in sys.argv[1:]:

    with open(tiedosto) as json_data:
        date = json.load(json_data)
        json_data.close()

        for tweet in date:
            aika = datetime.datetime.fromtimestamp(
                    int(tweet['time'])
                ).strftime('%Y-%m-%d')

            if aika not in laskuri:
                laskuri[aika] = 0

            laskuri[aika] += 1

            teksti_lista = tweet['text']
        
            for y in range(0, teema_lasku):

                teemat_lista.append({}) 

                if aika not in teemat_lista[y]:
                    teemat_lista[y][aika] = 0
            
                flag = False
                for x in jako[y]:
                    if x in teksti_lista and flag == False:
                        teemat_lista[y][aika] += 1
                        flag = True
                    
    for paiva in sorted( laskuri.keys()):
        teema_tulostus = ''
        for tulostus in range(0, teema_lasku):
            teema_tulostus += str(teemat_lista[tulostus][paiva]) + " , "
        print paiva , "," , laskuri[ paiva ], "," , teema_tulostus






