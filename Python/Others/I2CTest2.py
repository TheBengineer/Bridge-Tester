import commands, time
import smbus

f = [63, 6, 91, 79, 102, 109, 125, 7, 127, 111, 119, 124, 57, 94, 121, 113, 123]

bus = smbus.SMBus(1)
wait = .1

address = 0x48

while 1:
    t = time.time()
    for j in range(1000):
        data = 0x80e0
        bus.write_byte_data(address,0x01,data)
        for i in range(6):
            response = bus.read_word_data(address,0x00)
            #ADC = commands.getoutput("i2cset -y 1 0x60 0x44 "+hex(data))
            #time.sleep(wait)
            #print data, hex(data), response, hex(response)
            #data = data *2
    print time.time()-t



