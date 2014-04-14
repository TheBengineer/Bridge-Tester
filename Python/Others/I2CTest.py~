import commands, time

wait = .1

while 1:
    data = 16
    for i in range(4):
        ADC = commands.getoutput("i2cset -y 1 0x60 0x44 "+hex(data))
        time.sleep(wait)
        print data, hex(data)
        data = data *2



