
import socket, glob, json
from constants import Server
from messageParser import *

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((Server.IP.value, Server.PORT.value))



# https://www.w3resource.com/python/python-bytes.php#bytes_to_hex

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
    # print("[CORRECT] Transaction id is ", TransactionID)
    Flags = Header.getFlags(data[2:4])
    QuestionCount = Header.getQuestionCount(data[4:6])
    # print(int(QuestionCount))
    AnswerCount = Header.getAnswerCount(data[6:8])
    # print(int(AnswerCount))
    NSCOUNT = Header.getNsCount(data[8:10])
    # print(int(NSCOUNT))
    ARCOUNT = Header.getNsCount(data[10:12])
    # print(int(ARCOUNT))


    #   return int(QR+OPCODE+AA+TC+RD, 2).to_bytes(1, byteorder='big')+int(RA+Z+RCODE, 2).to_bytes(1, byteorder='big')
    # return(TransactionID.to_bytes(2, byteorder='big') + Flags.to_bytes(2, byteorder='big') + QuestionCount.to_bytes(2, byteorder='big') + AnswerCount.to_bytes(2, byteorder='big') + NSCOUNT.to_bytes(2, byteorder='big') + ARCOUNT.to_bytes(2, byteorder='big'))
    return bytes(TransactionID, 'utf-8') # TODO: have to complete parse header



def parseQuestion(data):
    # print(data[12:])
    return Header.getQuestionDomain(data[12:])



while True:
    data, addr = s.recvfrom(Server.MSGSIZE.value)
    # print(parseHeader(data))
    parseQuestion(data)
    # s.sendto(data, addr) 
    # print("RAW DATA: ", data)
