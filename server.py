""" 
Simple DNS Server




- TODO: We assume messages will be 512 bytes for now. Update code that it will allow a dynamic size. 
You can do this by using the truncation bit.
- TODO: We offer recursion in the end. 
"""

import socket, glob, json
from constants import Server

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((Server.IP.value, Server.PORT.value))

def load_zones():
    jsonzone = {}
    zonefiles = glob.glob('zones/*.zone')

    for zone in zonefiles:
        with open(zone) as zonedata:
            data = json.load(zonedata)
            zonename = data["$origin"]
            jsonzone[zonename] = data
    return jsonzone

zonedata = load_zones() #global

def getFlags(flags): # flags is third and fourth byte header

    # A the flags are bits in 2 bytes we have to use the bitshift operators to gain access to bit level indirectly
    # bit shifting is best done per byte, so we seperate the two combined ones into two separate ones
    byte1 = bytes(flags[:1]) # QR (1 bit) | Opcode (4 bits) | AA (1 bit)| TC (1 bit) | RD (1 bit)
    byte2 = bytes(flags[1:2]) # RA (1 bit) | Z (3 bits) | RCODE (4 bits)
    # print(flags1)

    QR = '1' # Question or response, when parsing a query you generate a response so always 1

    OPCODE = ''
    for bit in range(1, 5): # bit 1, 2, 3, 4 = OPCODE
        OPCODE += str(ord(byte1)&(1<<bit))

    AA = '1'
    TC = '0'
    RD = '0'
    #Byte 2
    RA = '0'
    Z = '000'
    RCODE = '0000'
    return (int(QR+OPCODE+AA+TC+RD, 2).to_bytes(1, byteorder='big')) + (int(RA+Z+RCODE, 2).to_bytes(1, byteorder='big'))


def getQuestionDomain(query):
    state = 0
    expectedLength = 0
    domainstring = ''
    domainparts = []
    x = 0
    y = 0
    for byte in query: # goes through every byte of query
        if state == 1:
            if byte != 0:
                domainstring += chr(byte) # so it does not result in integers convert to char
            x += 1
            if x == expectedLength:
                domainparts.append(domainstring)
                domainstring = ''
                state = 0
                x = 0
            if byte == 0:
                domainparts.append(domainstring)
                break
            
        else:
            state = 1
            expectedLength = byte # because before the domain name starts it tells in this byte how many characters it holds

        y += 1

    questiontype = data[y:y+2]

    return (domainparts, questiontype)

def getzone(domain):
    global zonedata

    zone_name = '.'.join(domain)

    return zonedata[zone_name]

def getrecs(data):
    domain, questiontype = getQuestionDomain(data)
    qt = ''
    if questiontype == b'\x00\x01':
        qt = 'a'

    zone = getzone(domain)

    return (zone[qt], qt, domain)
"""
                                    1  1  1  1  1  1
      0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                      ID                       | 16 bits is 2 bytes index = 0:2
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |QR|   Opcode  |AA|TC|RD|RA|   Z    |   RCODE   | index = 2:4
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    QDCOUNT                    | always 1 query in practice, 2 bytes
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    ANCOUNT                    | multiple answers possible
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    NSCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    ARCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
""" 
def parseQuery(data): 
    #TransactionID
    tIDString = data[0:2] # get first two bytes, which represent ID.
    tID = ''
    for byte in tIDString:
        tID += hex(byte)[2:] # removes 0x of hexadecimal
    print("[CORRECT] Transaction id is ", tID)

    Flags = getFlags(data[2:4])
    print(Flags)

    # Question count
    QDCOUNT = b'\x00\x01'
    # Answer count (will vary depending on the answers in ZONE file)
    # getQuestionDomain(data[12:]) # index 12 is from 13th byte, which is just after the header, which is the start of the query section
    print(getrecs(data[12:]))



    


    




while True:
    data, addr = s.recvfrom(Server.MSGSIZE.value)
    parseQuery(data)
    # s.sendto(data, addr) 