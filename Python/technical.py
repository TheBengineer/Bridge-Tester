def convertReading(readingraw):
        reading = int(readingraw/256)&0xff
        reading += (readingraw*256)&0xff00
	return reading

