import json
from pprint import pprint
import datetime
import sys

laskuri = {}

teemat = "teemat.txt"

tiedosto = open(teemat, 'r')

teemat = []

for line in tiedosto:
    line = line.strip()
    teemat.append(line.split(","))

laskuri_teemat = []

for i in teemat:
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

            viesti = tweet['text']

            for y in range(0, len( teemat ) ):

                flag = False

                if aika not in teemat[y]:
                    laskuri_teemat[y][aika] = 0

                for termi in teemat[y]:

                    if termi in viesti and not flag:
                        laskuri_teemat[y][aika] += 1
                        flag = True


    for paiva in sorted( laskuri.keys() ):
        teema_tulostus = ''

        for tulostus in range(0, len( teemat ) ):
            teema_tulostus += str( laskuri_teemat[tulostus][paiva]) + " , "

        print paiva , "," , laskuri[ paiva ], "," , teema_tulostus
