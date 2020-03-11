byte = b'00000000'
# convert the byte to an integer representation
byte = ord(byte)
# now convert to string of 1s and 0s
byte = bin(byte)[2:].rjust(8, '0')
# now byte contains a string with 0s and 1s
for bit in byte:
    print(bit)
