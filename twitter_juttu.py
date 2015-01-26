import json
from pprint import pprint
import datetime
import sys
import collections

teemat = []

for rivi in open( sys.argv[ -1 ] , 'r'):
    rivi = rivi.strip()
    rivi = rivi.split(',')
    rivi = map( lambda x: x.strip() , rivi )
    teemat.append( rivi )

laskuri = [ collections.defaultdict( int ) ]

for i in teemat:
    laskuri.append( collections.defaultdict( int ) )

for tiedosto in sys.argv[ 1: -1 ]:

    tweets = json.load( open( tiedosto , 'r' ) )

    for tweet in tweets:

        aika = datetime.datetime.fromtimestamp( int(tweet['time']) ).strftime('%Y-%m-%d')

        laskuri[0][aika] += 1

        viesti = tweet['text']

        for y in range(0, len( teemat ) ):

            flag = False

            for termi in teemat[y]:

                if termi in viesti and not flag:
                    laskuri[y + 1][aika] += 1
                    flag = True

for paiva in sorted( laskuri[0].keys() ):

    tiedot = []

    for rivi in laskuri:
        tiedot.append( rivi[paiva] )

    tiedot = map( str, tiedot )

    print paiva + ',' + ','.join( tiedot )
