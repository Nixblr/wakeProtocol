import enum

#############################################################
#						Wake frame format                   #
#   | FEND | ADDR | CMD | LEN | Data0 | … | DataN | CRC |   #
#############################################################

__version__ = '1.0.0'

class escapesym(enum.IntEnum):
    FEND = 0xc0     #Frame END
    FESC = 0xDB     #Frame Escape
    TFEND = 0xDC    #Transponded Frame End
    TFESC = 0xDD    #Transponded Frame Escape