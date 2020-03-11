
import socket, glob, json
from constants import Server
from messageParser import *

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((Server.IP.value, Server.PORT.value))





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
def parseHeader(data):

    TransactionID = Header.getTransactionID(data)
    print("[CORRECT] Transaction id is ", TransactionID)
    Header.getFlags(data[2:4])
    questionCount = Header.getQuestionCount(data[4:6])

while True:
    data, addr = s.recvfrom(Server.MSGSIZE.value)
    parseHeader(data)
    # s.sendto(data, addr) 