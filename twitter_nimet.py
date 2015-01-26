import json
import datetime
import sys

laskuri = {}

for tiedosto in sys.argv[1:]:

    with open(tiedosto) as json_data:
        tieto = json.load(json_data)
        json_data.close()
    
        for tweet in tieto:

            nimi_lista = tweet['from_user']

            if nimi_lista not in laskuri:
                laskuri[nimi_lista] = 0

            laskuri[nimi_lista] += 1

    for nimi in sorted( laskuri.keys()):
        print nimi




