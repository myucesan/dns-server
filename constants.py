from enum import Enum
# Server (UDP)
class Server(Enum):
    IP = "127.0.0.1"
    # IP = "localhost"
    PORT = 53
    MSGSIZE = 512
# Size limits (in octet)
class SizeLimits(Enum):
    LABELS = 64
    NAMES = 255
    UDPM = 512
    TTL = 10 #positive values of a signed 32 bit number

# QTYPE values (appear in question part of a query) (superset of TYPE, TYPE's are valid QTYPE's)
class QTYPE(Enum):
    AXFR = 252 # A request for transfer of an entire zone
    MAILB = 253 # A request for mailbox-related records (MV, MG, or MR)
    MAILA = 254 # A request for mail agent RRs (Obsolete - see MX)
    ASTERISK = 255 # A request for all records
    
# TYPE values (subset of QTYPE) (resource records)
class TYPE(Enum):

    A = 1 # a host address
    NS = 2 # an authoritative name server
    MD = 3 # a mail destination (Obsolete - use MX)
    MF = 4 # a mail forwarder (Obsolete - use MX)
    CNAME = 5 # the canonical name for an alias
    SOA = 6 # marks the start of a zone of authority
    MB = 7 # a mailbox domain name (EXPERIMENTAL)
    MG = 8 # a mail group member (EXPERIMENTAL)
    MR = 9 # a null RR (EXPERIMENTAL)
    NULL = 10 # a null RR (EXPERIMENTAL)
    WKS = 11 # a well known service description
    PTR = 12 # a domain name pointer
    HINFO = 13 # host information
    MINFO = 14 # mailbor or mail list information
    MX = 15 # mail exchange
    TXT = 16 # text strings



# QCLASS values (appear in question section of query, superset of CLASS values so every class is a valid QCLASS)
class QCLASS(Enum):
    QCLASSASTERISK = 255 # any class

# CLASS values (appear in resource records)
class CLASS(Enum):
    IN = 1 # the Internet
    CS = 2 # the CSNET class (Obsolete - used only for examples in some obsolete RFCs)
    CH = 3 # the chaos class
    HS = 4 # Hesiod [Dyer 87]



