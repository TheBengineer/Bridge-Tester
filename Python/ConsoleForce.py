import  random, sys, math,time,commands,os
import smbus

address = 0x49 # Address of ADC
bus = smbus.SMBus(1) # connect to IIC line # 1
bus.write_word_data(address,0x01,0x80E0) # Default setup
wait = .2
while 1:
	readingraw = bus.read_word_data(address,0x00)
	reading = int(readingraw/256)&0xff        
	reading += (readingraw*256)&0xff00
	#print reading, hex(reading), hex(readingraw)
	print 
	try:
	    ADCNormalized = reading*2/655.35
	except:
	    print "I2c Error"
	    ADCNormalized = 0
	print ADCNormalized,
	if ADCNormalized < 3:
        	for i in range(int(ADCNormalized*10)):
			sys.stdout.write("#")
	time.sleep(wait)
