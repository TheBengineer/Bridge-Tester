import time	


while 1:
    t = time.time()
    for i in xrange(100000):
        x = t-time.time()
    print "mS to time.time()",(time.time()-t)/100


