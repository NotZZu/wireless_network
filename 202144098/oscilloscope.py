import sys
import tos
import datetime
import threading

AM_OSCILLOSCOPE = 0x93

class OscilloscopeMsg(tos.Packet):
    def __init__(self, packet = None):
        tos.Packet.__init__(self,
                [('srcID', 'int', 2),
                    ('seqNo', 'int', 4),
                    ('type', 'int', 2),
                    ('Data0', 'int', 2),
                    ('Data1', 'int', 2),
                    ('Data2', 'int', 1),
                    ('Data3', 'int', 1),
                    ('Data4', 'int', 2),
                    ],
                packet)

if '-h' in sys.argv:
    print "Usage:", sys.argv[0], "serial@/dev/ttyUSB0:57600"
    sys.exit()

am = tos.AM()

while True:
    p = am.read()
    msg = OscilloscopeMsg(p.data)
    print p

    if msg.type == 2:
        battery = msg.Data4

        Illumi = int(msg.Data2)+ int(msg.Data3*256)
        Illumi = Illumi
        humi = -2.0468 + (0.0367*msg.Data1) + (-1.5955*0.




