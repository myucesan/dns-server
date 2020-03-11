
class Header():

    @staticmethod
    def getTransactionID(data):
        tIDString = data[0:2] # get first two bytes, which represent ID.
        tID = ''
        for byte in tIDString:
            tID += hex(byte)[2:] # removes 0x of hexadecimal

        return tID

    @staticmethod
    def getFlagsOld(flags): # flags is third and fourth byte header

    @staticmethod
    def getFlags(flags): # flags is third and fourth byte header

        # A the flags are bits in 2 bytes we have to use the bitshift operators to gain access to bit level indirectly
        # bit shifting is best done per byte, so we seperate the two combined ones into two separate ones
        byte1 = bytes(flags[:1]) # QR (1 bit) | Opcode (4 bits) | AA (1 bit)| TC (1 bit) | RD (1 bit)
        byte2 = bytes(flags[1:2]) # RA (1 bit) | Z (3 bits) | RCODE (4 bits)


    @staticmethod
    def getQuestionCount(data): 
        print(1)