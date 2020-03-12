
from constants import Server
class Header():

    @staticmethod
    def getTransactionID(data):
        tIDString = data[0:2] # get first two bytes, which represent ID.
        tID = ''
        for byte in tIDString:
            tID += hex(byte)[2:] # removes 0x of hexadecimal

        return tID

    '''
    Z is 010, the query format does not comply with the header format in the rfc. FIX by forcing 0 because Z always has to be zero.
    '''
    @staticmethod
    def getFlags(flags): # flags is third and fourth byte header

        # TODO - The code is explicitly checking each index of flagbytes but this can be done more efficiently.
        # A the flags are bits in 2 bytes we have to use the bitshift operators to gain access to bit level indirectly
        # bit shifting is best done per byte, so we seperate the two combined ones into two separate ones
        flagBytes = []
        for byte in flags:
            appender = bin(byte)[2:]
            print(appender)
            flagBytes.append(appender)

        bitsMissing = Server.BYTE.value - len(flagBytes[0])
        print("So many bits are missing: ", bitsMissing)

        for x in range(bitsMissing):
            flagBytes[0] = "0" + flagBytes[0]

        bitsMissing = Server.BYTE.value - len(flagBytes[1])
        print("So many bits are missing: ", bitsMissing)

        for x in range(bitsMissing):
            flagBytes[1] = "0" + flagBytes[1]

        # print("Flags 1 = ", flagBytes[0]) # QR (1 bit) | Opcode (4 bits) | AA (1 bit)| TC (1 bit) | RD (1 bit)
        # print("Flags 2 = ", flagBytes[1]) # RA (1 bit) | Z (3 bits) | RCODE (4 bits)


        # print("Bits in Byte 1")

        # print("QR = ", flagBytes[0][0])
        # print("OPCODE = ", flagBytes[0][1] + flagBytes[0][2] + flagBytes[0][3] + flagBytes[0][4])
        # print("AA = ", flagBytes[0][5])
        # print("TC = ", flagBytes[0][6])
        # print("RD = ", flagBytes[0][7])

        # print("Bits in Byte 2")

        # print("RA = ", flagBytes[1][0])
        # print("Z = ", flagBytes[1][1] + flagBytes[1][2] + flagBytes[1][3])
        # print("RCODE = ", flagBytes[1][4] + flagBytes[1][5] + flagBytes[1][6] + flagBytes[1][7])

        return(int(flagBytes[0][0]+flagBytes[0][1] + flagBytes[0][2] + flagBytes[0][3] + flagBytes[0][4]+ flagBytes[0][5] + flagBytes[0][6] + flagBytes[0][7], 2).to_bytes(1, byteorder='big') + int(flagBytes[1][0] + flagBytes[1][1] + flagBytes[1][2] + flagBytes[1][3] + flagBytes[1][4] + flagBytes[1][5] + flagBytes[1][6] + flagBytes[1][7], 2).to_bytes(1, byteorder='big'))


    @staticmethod        
    def getQuestionCount(questionCount): # flags is third and fourth byte header
        qCount = ''
        for byte in questionCount:
           qCount += hex(byte)[2:]
        
        return qCount

    @staticmethod        
    def getAnswerCount(answerCount): # flags is third and fourth byte header
        aCount = ''
        for byte in answerCount:
           aCount += hex(byte)[2:]
        
        return aCount

    @staticmethod        
    def getNsCount(nsCount): # flags is third and fourth byte header
        # print(nsCount)
        nCount = ''
        for byte in nsCount:
           nCount += hex(byte)[2:]
        
        return nCount

    @staticmethod        
    def getArCount(arCount): # flags is third and fourth byte header
        # print(arCount)
        Count = ''
        for byte in arCount:
           Count += hex(byte)[2:]
        
        return Count

    @staticmethod
    def getQuestionDomain(data):
        # print(data[0:7])
        return data[0:]