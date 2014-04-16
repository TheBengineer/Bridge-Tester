def convertReading(readingraw):
    reading = int(readingraw/256)&0xff
    reading += (readingraw*256)&0xff00
    if reading > 0x7fff:
        reading = 0
    return reading

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)