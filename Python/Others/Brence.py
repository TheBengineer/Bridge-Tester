#!/usr/bin/env python
def getsystem():
    import os
    return os.sys.platform
def getlocalip():
    import os
    if os.sys.platform == "win32":
        back = os.popen("ipconfig /all")
        cmd = back.read(2000)
        cmd2 = cmd[cmd.find("IP Address"):cmd.find("IP Address")+70]
        cmd3 = cmd2[cmd2.find(":")+2:cmd2.find(":")+19]
        c4 = cmd3[0:cmd3.find(" ")-2]
    if os.sys.platform == "linux2":
        back = os.popen("ifconfig")
        cmd = back.read(2000)
        cmd2 = cmd[cmd.find("Ethernet"):cmd.find("Ethernet")+300]
        cmd3 = cmd2[cmd2.find("inet addr:")+10:cmd2.find("inet addr:")+50]
        c4 = cmd3[0:cmd3.find(" ")]
    if c4 != "":
        return c4
    else:
        return "localhost"
def getscriptdir():
    import os
    if getsystem() == "win32":
        return str(os.getcwd())+"\\"
    if getsystem() == "linux2":
        return str(os.getcwd())+"/"
def getadd():
    local = getlocalip()
    host = raw_input("Type host, skip for "+str(local)+ ":")
    if host == "":
        host = local
    port = raw_input("Type port, skip for 90 :")
    if port:
        port = int(port)
    else:
        port = 90
    address = (host,port)
    return address
def gethost():
    local = getlocalip()
    host = raw_input("Type host, skip for "+str(local)+ ":")
    if host == "":
        return local
    else:
        return host
def host_socket(portbase):
    import socket
    socktmp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = False
    portmod = 0
    while connect == False:
        if portmod < 100:
            try:
                print "Hosting at localhost,",portbase+portmod
                socktmp.bind((getlocalip(), portbase+portmod))
                print "Hosting at localhost,",portbase+portmod, "successful"
                connect = True
                return socktmp,portbase+portmod
            except:
                print "Hosting at localhost,",portbase+portmod, "Failed"
                print "Next port"
                portmod += 1
        else:
            print "Cannot host at localhost", portbase, "~",portbase+portmod
            return None
def join_address(address,portbase):
    import socket
    connect = False
    portmod = 0
    while connect == False:
        if portmod < 100:
            try:
                socktmp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socktmp.settimeout(1)
                print "Connecting to",address,"at ",portbase+portmod
                socktmp.connect((address, portbase+portmod))
                print "Connecting to",address,"at ",portbase+portmod, "sucsessfull"
                connect = True
                if socktmp.recv(2):
                    socktmp.settimeout(240)
                    print "listen for port from",address,":",portbase+portmod
                    port = socktmp.recv(10)
                    return port
            except socket.timeout:
                print "Connecting to",address,"at ",portbase+portmod, "Timeout"
                print "Next port"
                connect = False
                portmod += 1
                socktmp.close()
            except socket.error:
                print "Connecting to",address,"at ",portbase+portmod, "Timeout"
                print "Next port"
                connect = False
                portmod += 1
                socktmp.close()
        else:
            print "cannot Connect to",address
            return None
def timesynchost():
    import time
    import socket
    timesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    timesocket.bind((getlocalip(),4999))
    timesocket.listen(1)
    timeclient, clientaddress = timesocket.accept()
    rtimes = []
    ltimes = []
    tm = time.time()
    error = time.time()-tm
    for i in range(10):
        rtimes.append(timeclient.recv(64))
        t = str(time.time())
        timeclient.send(t)
        ltimes.append(t)

def timesyncconnect():
    import time
    import socket
    timesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    timesocket.connect((gethost(), 4999))
    rtimes = []
    ltimes = []
    for i in range(10):
        t = str(time.time())
        timesocket.send(t)
        ltimes.append(t)
        rtimes.append(timesocket.recv(64))
        print i
    timesocket.close()

def writeCSV(Data,Dir,filename): #2D data only
    import os
    line = ""
    lines = []
    if os.path.exists(Dir):
        f = open(Dir+filename,'w')
        for i in Data:
            for j in i:
                line += str(j) +","
            line += "\n"
            f.writelines(line)
            line = ""
        f.close()
        return 0
    else:
        return 1
def readCSV(filename):
    import os
    data = []
    if os.path.isfile(filename):
        f = open(filename, "r")
        lines = f.readlines()
        #print lines
        for i in lines:
            #print i[-2]
            if i[-2]!= ",":
                i = i[:-1]+","
            j =i.split(",")[:-1]
            for k in range(len(j)):
                try:
                    j[k] = int(j[k])
                except ValueError:
                    try: j[k] = float(j[k])
                    except: pass
            data.append(j)
        f.close()
    return data

writeCSV([[1,2],[3,4],[5.1,6.0],[7,[8,9]]],"/tmp/","test")
print readCSV("/tmp/test")
