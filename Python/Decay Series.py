import Decay

test = ""
while 1:
    test = "207Pb"
    test = str(raw_input("Isotope: "))
    print "Starting Isotope: ",test
    Decay.test_decay(test)
