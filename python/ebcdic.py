#!/usr/bin/env python3

pre = "\xab\xcd\x00\x01\x35\x11\x00\x27"
post = "\x3c\x11"

ascii = ['[NUL]','[SOH]','[STX]','[ETX]',
         '[PF]','[HT]','[LC]','[DEL]',
         '[GE]','[RLF]','[SMM]','[VT]',
         '[FF]','[CR]','[SO]','[SI]',
         '[DLE]','[DC1]','[DC2]','[TM]',
         '[RES]','[NL]','[BS]','[IL]',
         '[CAN]','[EM]','[CC]','[CU1]',
         '[IFS]','[IGS]','[IRS]','[IUS]',
         '[DS]','[SOS]','[FS]','[0x23]',
         '[BYP]','[LF]','[ETB]','[ESC]',
         '[0x28]','[0x29]','[SM]','[CU2]',
         '[0x2C]','[ENQ]','[ACK]','[BEL]',
         '[0x30]','[0x39]','[0x3A]','[CUB]',
         '[DC4]','[NAK]','[0x3E]','[SUB]',
         ' ','[0x41]','[0x42]','[0x43]',
         '[0x44]','[0x45]','[0x46]','[0x47]',
         '[0x48]','[0x49]','[cent]','.',
         '<','(','+','[vert line]',
         '&','[0x51]','[0x52]','[0x53]',
         '[0x54]','[0x55]','[0x56]','[0x57]',
         '[0x58]','[0x59]','!','$',
         '*',')',';','[not equal]',
         '-','/','[0x62]','[0x63]',
         '[0x64]','[0x65]','[0x66]','[0x67]',
         '[0x68]','[0x69]','|',',',
         '%','_','>','?',
         '[0x70]','[0x71]','[0x72]','[0x73]',
         '[0x74]','[0x75]','[0x76]','[0x77]',
         '[0x78]','`',':','#',
         '@','\'','=','"',
         '[0x80]','a','b','c',
         'd','e','f','g',
         'h','i','[0x8A]','[0x8B]',
         '[0x8C]','[0x8D]','[0x8E]','[0x8F]',
         'j','k','l','m',
         'n','o','p','q',
         'r','[0x9A]','[0x9B]','[0x9C]',
         '[0x9D]','[0x9E]','[0x9F]','[0xA0]',
         '~','s','t','u',
         'v','w','x','y',
         'z','[0xAA]','[0xAB]','[0xAC]',
         '[0xAD]','[0xAE]','[0xAF]','[0xB0]',
         '[0xB1]','[0xB2]','[0xB3]','[0xB4]',
         '[0xB5]','[0xB6]','[0xB7]','[0xB8]',
         '[0xB9]','[0xBA]','[0xBB]','[0xBC]',
         '[0xBD]','[0xBE]','[0xBF]','{',
         'A','B','C','D',
         'E','F','G','H',
         'I','[0xCA]','[0xCB]','[non-displayable 0xCC]',
         '[0xCD]','[non-displayable 0xCE]','[0xCF]','}',
         'J','K','L','M',
         'N','O','P','Q',
         'R','[0xDA]','[0xDB]','[0xDC]',
         '[0xDD]','[0xDE]','[0xDF]','\\',
         '[0xE1]','S','T','U',
         'V','W','X','Y',
         'Z','[0xEA]','[0xEB]','[non-displayable 0xEC]',
         '[0xED]','[0xEE]','[0xEF]','0',
         '1','2','3','4',
         '5','6','7','8',
         '9','[non-displayable 0xEF]','[0xFA]','[0xFB]',
         '[0xFC]','[0xFD]','[0xFE]','[E0]']

def printascii(ebcdic_string):
    for x in range(0, len(ebcdic_string)):
        sys.stdout.write(ascii[ebcdic_string[x]])


def getascii(ebcdic_string):
    my_string = ""
    for x in range(0, len(ebcdic_string)):
        my_string += ascii[ebcdic_string[x]]
    return my_string


def getebcdic(string):
    my_string = b''
    for x in range(0, len(string)):
        for y in range(0, len(ascii)):
            if string[x] == ascii[y]:
                my_string == y.to_bytes(1, 'little')
    return(my_string)
