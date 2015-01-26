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

laskuri_teemat = []

teemat_lista = jako

for i in teemat_lista:
    laskuri_teemat.append( {} )

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

                flag = False

                if aika not in teemat_lista[y]:
                    laskuri_teemat[y][aika] = 0

                for x in teemat_lista[y]:
                    if x in teksti_lista and not flag:
                        laskuri_teemat[y][aika] += 1
                        flag = True


    for paiva in sorted( laskuri.keys() ):
        teema_tulostus = ''
        for tulostus in range(0, teema_lasku):
            teema_tulostus += str( laskuri_teemat[tulostus][paiva]) + " , "
        print paiva , "," , laskuri[ paiva ], "," , teema_tulostus
