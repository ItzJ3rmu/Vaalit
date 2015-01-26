import json
from pprint import pprint
import datetime
import sys

teemat = "teemat.txt"

tiedosto = open(teemat, 'r')

teemat = []

for line in tiedosto:
    line = line.strip()
    teemat.append(line.split(","))

laskuri = [ {} ]

for i in teemat:
    laskuri.append( {} )

for tiedosto in sys.argv[1:]:

    with open(tiedosto) as json_data:
        date = json.load(json_data)
        json_data.close()

        for tweet in date:
            aika = datetime.datetime.fromtimestamp(
                    int(tweet['time'])
                ).strftime('%Y-%m-%d')

            if aika not in laskuri:
                laskuri[0][aika] = 0

            laskuri[0][aika] += 1

            viesti = tweet['text']

            for y in range(0, len( teemat ) ):

                flag = False

                if aika not in teemat[y]:
                    laskuri[y + 1][aika] = 0

                for termi in teemat[y]:

                    if termi in viesti and not flag:
                        laskuri[y + 1][aika] += 1
                        flag = True


    for paiva in sorted( laskuri[0].keys() ):
        teema_tulostus = ''

        for tulostus in range(0, len( teemat ) ):
            teema_tulostus += str( laskuri[tulostus + 1][paiva]) + " , "

        print paiva , "," , laskuri[ 0 ][ paiva ], "," , teema_tulostus
