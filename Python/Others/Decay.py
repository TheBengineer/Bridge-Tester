#Mass chain dictionary
#(Probability1,Half_Life,Type,Energy,"Product Name")
# {"Start Name":((Probability1,Half_Life,Type,Energy,"Product Name"),((Probability1,Half_Life,Type,Energy,"Product Name"))}


class Decay():
    Decay = {
    "244Pu": (1, (3, 2522880000000000L, 0, 4.589, '240U')) ,
    "218At": (2, (0.001, 1.5, 1, 2.883, '218Rn'), (0.999, 1.5, 0, 6.874, '214Bi')) ,
    "221Fr": (1, (1, 288, 0, 6.3, '217At')) ,
    "209Bi": (1, (1, 599184000000000000000000000L, 0, 3.137, '205Tl')) ,
    "211Bi": (2, (0.00276, 128.4, 1, 0.575, '211Po'), (99.724, 128.4, 0, 6.751, '207Tl')) ,
    "219Rn": (1, (1, 3.96, 0, 6.946, '215Po')) ,
    "210Bi": (2, (1.3e-06, 433123.2, 0, 5.982, '206Tl'), (0.9999987, 433123.2, 1, 1.426, '210Po')) ,
    "218Po": (2, (0.0002, 186, 1, 0.265, '218At'), (0.9989, 186, 0, 6.115, '214Pb')) ,
    "228Ac": (1, (10, 22500, 1, 2.124, '228Th')) ,
    "214Po": (1, (1, 0.0001643, 0, 7.883, '210Pb')) ,
    "228Th": (1, (11, 60284217.6, 0, 5.52, '224Ra')) ,
    "245Cm": (1, (1, 268056000000L, 0, 5.537, '241Pu')) ,
    "215Po": (2, (2.3e-06, 0.001781, 1, 0.715, '215At'), (0.9999977, 0.001781, 0, 7.527, '211Pb')) ,
    "213Bi": (2, (0.22, 2790, 0, 5.87, '209Tl'), (0.978, 2790, 1, 1.423, '213Po')) ,
    "240Pu": (1, (6, 206907696000L, 0, 5.1683, '236U')) ,
    "214Pb": (1, (1, 1608, 1, 1.024, '214Bi')) ,
    "233U": (1, (1, 5020531200000L, 0, 4.909, '229Th')) ,
    "206Tl": (1, (1, 251.94, 1, 1.533, '206Pb')) ,
    "227Th": (1, (1, 1613952, 0, 6.147, '223Ra')) ,
    "248Cm": (1, (2, 10722240000000L, 0, 5.162, '244Pu')) ,
    "212Po": (1, (1, 2.99e-07, 0, 8.955, '208Tl')) ,
    "212Pb": (1, (15, 38304, 1, 0.57, '212Bi')) ,
    "241Am": (1, (1, 13645627200L, 0, 5.638, '237Np')) ,
    "215Bi": (1, (1, 456, 1, 2.25, '215Po')) ,
    "213Po": (1, (1, 3.72e-05, 0, 8.536, '209Pb')) ,
    "214Bi": (2, (0.0002, 1194, 0, 5.617, '210Tl'), (0.9998, 1194, 1, 3.272, '214Po')) ,
    "206Pb": (1, (1, 31536000, 2, 0, '206Pb')) ,
    "218Rn": (1, (1, 0.035, 0, 7.263, '214Po')) ,
    "219At": (2, (0.03, 56, 1, 1.7, '219Rn'), (0.97, 56, 0, 6.275, '215Bi')) ,
    "223Ra": (1, (1, 987552, 0, 5.979, '219Rn')) ,
    "207Tl": (1, (1, 286.2, 1, 1.418, '207Pb')) ,
    "220Rn": (1, (13, 55.6, 0, 6.404, '216Po')) ,
    "207Pb": (1, (1, 31536000, 2, 0, '207Pb')) ,
    "235U": (1, (1, 22201344000000000L, 0, 4.678, '231Th')) ,
    "234U": (1, (1, 7742088000000L, 0, 4.859, '230Th')) ,
    "234mPa": (2, (0.0016, 69.6, 2, 0.074, '234Pa'), (0.9984, 69.6, 1, 2.271, '234U')) ,
    "230Th": (1, (1, 2377183680000L, 0, 4.77, '226Ra')) ,
    "239Pu": (1, (1, 760017600000L, 0, 5.244, '235U')) ,
    "231Th": (1, (1, 91872, 1, 0.391, '231Pa')) ,
    "208Tl": (1, (1, 183.18, 1, 4.999, '208Pb')) ,
    "208Pb": (1, (1, 31536000, 2, 0, '208Pb')) ,
    "240Np": (1, (5, 3715.2, 1, 2.2, '240Pu')) ,
    "225Ac": (1, (1, 864000, 0, 5.935, '221Fr')) ,
    "240U": (1, (4, 50760, 1, 0.39, '240Np')) ,
    "238U": (1, (1, 140902848000000000L, 0, 4.27, '234Th')) ,
    "227Ac": (2, (0.0138, 686601792, 0, 5.042, '223Fr'), (0.9862, 686601792, 1, 0.045, '227Th')) ,
    "249Cf": (1, (1, 11069136000L, 0, 6.201, '245Cm')) ,
    "232Th": (1, (8, 443080800000000000L, 0, 4.081, '228Ra')) ,
    "236U": (1, (7, 725328000000000L, 0, 4.494, '232Th')) ,
    "241Pu": (1, (1, 454118400, 1, 0.021, '241Am')) ,
    "231Pa": (1, (1, 1033119360000L, 0, 5.15, '227Ac')) ,
    "216Po": (1, (14, 0.145, 0, 6.906, '212Pb')) ,
    "234Th": (1, (1, 2082240, 1, 0.273, '234mPa')) ,
    "217At": (1, (1, 0.032, 0, 7, '213Bi')) ,
    "223Fr": (2, (6e-05, 1320, 0, 5.34, '219At'), (0.99994, 1320, 1, 1.149, '223Ra')) ,
    "234Pa": (1, (1, 24120, 1, 2.197, '234U')) ,
    "233Pa": (1, (1, 2332800, 1, 0.571, '233U')) ,
    "212Bi": (2, (0.3594, 3633, 0, 6.208, '212Po'), (0.6406, 3633, 1, 2.252, '212Po')) ,
    "205Tl": (1, (1, 31536000, 2, 0, '205Tl')) ,
    "237Np": (1, (1, 67487040000000L, 0, 4.959, '233Pa')) ,
    "229Th": (1, (1, 231474240000L, 0, 5.168, '225Ra')) ,
    "228Ra": (1, (9, 181332000, 1, 0.046, '228Ac')) ,
    "225Ra": (1, (1, 1287360, 1, 0.36, '225Ac')) ,
    "226Ra": (1, (1, 50520672000L, 0, 4.871, '222Rn')) ,
    "215At": (1, (1, 0.001, 0, 8.178, '211Bi')) ,
    "211Pb": (1, (1, 2166, 1, 1.367, '211Bi')) ,
    "209Pb": (1, (1, 11700, 1, 0.644, '209Bi')) ,
    "209Tl": (1, (1, 132, 1, 3.99, '209Pb')) ,
    "210Po": (1, (1, 11955686.4, 0, 5.407, '206Pb')) ,
    "210Tl": (1, (1, 78, 1, 5.484, '210Pb')) ,
    "222Rn": (1, (1, 330350.4, 0, 5.59, '218Po')) ,
    "210Pb": (1, (1, 703252800, 1, 0.064, '210Bi')) ,
    "224Ra": (1, (12, 313796.16, 0, 5.789, '220Rn')) ,
    "211Po": (1, (1, 0.516, 0, 7.595, '207Pb')) ,
    "252Cf": (1, (1, 83412720, 0, 6.1181, '248Cm')) ,
    }


def test_decay(isotope):
    c = Decay.Decay
    run = 1
    b = isotope
    energy = 0.0
    time = 0
    while run:
        a = c[b]
        print a
        energy += a[1][3]
        time += a[1][1]
        if a[1][4] == b:
            print "STABLE"
            run = 0
        b = a[1][4]
    halflife = time/63072000
    print "Total energy:",str(energy)+"eV"
    print "Total time:",str(time)+"Years"
