#!/usr/bin/python3i

import sys

for line in sys.stdin:
        line = line.strip()
        line = line.split(',')

        #SongId = line[0]
        #AlbumID = line[1]
        #AlbumName = line[2]
        #ArtistID = line[3]
	#ArtistLatitude = line[4]
        #ArtistLocation = line[5]
        #ArtistLongitude = line[6]
        #ArtistName = line[7]
        #danceability = float(line[8])
        #Duration = line[9]
        #KeySignature = line[10]
        #KeySignatureConfidence = line[11]
        tempo = float(line[12])
        #TimeSignature = line[13]
        #TimeSignatureConfidence = line[14]
        #Title = line[15]
        year = int(line[16])
        hotness = float(line[17])
        #print(tempo)
        if hotness > 0.5:
                if (year > 0 and tempo > 0):
                    print('%s \t %s' % (year, tempo))
