# coding: utf-8
import struct

def rotateLeft(b):
    res = b << 1
    v = (b >> 0x1f) & 0x1
    res = v | res
    return res & 0xFFFFFFFF

def do16(block, init):
    for i in range(15, -1, -1):
        print i
        inter = internal[i] << 8*3
        inter |= internal[i+1] << 8*2
        inter |= internal[i+2] << 8
        inter |= internal[i+3]
        #inter = int(''.join([hex(v).replace('0x', '') for v in internal[i:i+4]]), 16)
        print hex(inter)
        step1 = block^inter
        print "Initial block: " + hex(block)
        print "Step1: " + hex(step1)
        step2 = rotateLeft(step1)
        print "Step2: " + hex(step2)
        byte1 = (step2 >> 8*3)&0xff
        byte2 = (step2 >> 8*2)&0xff
        byte3 = (step2 >> 8)&0xff
        byte4 = (step2)&0xff
        step3 = suboxy.index(byte1) << 8*3
        step3 |= suboxy.index(byte2) << 8*2
        step3 |= suboxy.index(byte3) << 8
        step3 |= suboxy.index(byte4)
        print "Step3: " + hex(step3)
        block = step3
        print "After stage 3: " + hex(step3)
        #take each byte find the index into suboxy
    return block^init




suboxy = ['0x21', '0x10', '0x1a', '0xe6', '0x15', '0xc8', '0xc5', '0x44', '0x96', '0xa0', '0x5d', '0xc7', '0xb8', '0xae', '0x55', '0x30', '0x1f', '0x04', '0xfc', '0x1b', '0xfe', '0xc4', '0x35', '0xef', '0xd1', '0x77', '0x43', '0x61', '0xc9', '0x9b', '0xe5', '0xa3', '0x0c', '0x40', '0x2f', '0xc0', '0xcf', '0x4d', '0xe7', '0xb0', '0x70', '0xd4', '0xfb', '0x6c', '0x88', '0xc1', '0x16', '0x65', '0xe9', '0x36', '0x80', '0x51', '0x53', '0x0a', '0xa2', '0xea', '0xdb', '0x05', '0x01', '0x0b', '0x8d', '0x4a', '0x68', '0x47', '0x25', '0x99', '0x02', '0xc6', '0xe0', '0x2b', '0x2d', '0x73', '0xf3', '0xfa', '0x27', '0x7e', '0xbb', '0xca', '0x06', '0xa4', '0xf9', '0x98', '0x97', '0xb5', '0x09', '0x12', '0x0e', '0x4f', '0x14', '0xfd', '0x41', '0xf7', '0x83', '0x6d', '0x52', '0x07', '0x75', '0x93', '0x74', '0x6f', '0x5a', '0xb1', '0xad', '0x28', '0x31', '0x18', '0x69', '0xa7', '0x3f', '0x48', '0xf1', '0x81', '0x85', '0x92', '0xdd', '0x3e', '0x3a', '0xe8', '0xc3', '0x34', '0xf4', '0x7f', '0x57', '0x62', '0x3b', '0xa8', '0xbe', '0xbc', '0xd7', '0xaa', '0xcc', '0xa5', '0xba', '0xab', '0xde', '0xaf', '0x8b', '0xe3', '0x58', '0x1e', '0x3d', '0x4b', '0xd3', '0xa1', '0x19', '0x84', '0x23', '0x95', '0xdc', '0xeb', '0x32', '0x9e', '0x72', '0x5c', '0x46', '0xa9', '0x5f', '0xee', '0x89', '0x1c', '0x49', '0x9d', '0x6b', '0x5e', '0x9f', '0x3c', '0x7d', '0x4e', '0xcd', '0x13', '0x2c', '0x2e', '0x56', '0x7a', '0xf2', '0xe1', '0xd6', '0x79', '0x8a', '0x63', '0x9c', '0x54', '0xda', '0x20', '0x0d', '0x76', '0xdf', '0xc2', '0xec', '0x50', '0xd0', '0x38', '0x67', '0xe4', '0xb2', '0x00', '0xb7', '0x8c', '0xf0', '0x5b', '0x82', '0x59', '0xe2', '0xac', '0xd9', '0xd2', '0x08', '0x6a', '0x45', '0xbf', '0xd8', '0x94', '0x4c', '0x17', '0x8e', '0x7b', '0xf8', '0xce', '0x42', '0x39', '0x29', '0x2a', '0xbd', '0x0f', '0x66', '0x22', '0x03', '0x6e', '0x1d', '0x60', '0x8f', '0x26', '0xf6', '0x37', '0x11', '0xb4', '0x9a', '0x91', '0xed', '0x64', '0x7c', '0x90', '0xb9', '0xb3', '0xb6', '0xf5', '0xcb', '0x86', '0x87', '0x33', '0x78', '0x24', '0xa6', '0xd5', '0x71', '0xff']
suboxy = [int(s[2:], 16) for s in suboxy]

internal = [0x59, 0x5e, 0x78, 0x2e, 0x47, 0x20, 0x85, 0xe1, 0x6c, 0x60, 0xa6, 0xdf, 0xb2, 0x77, 0x0c, 0x78, 0x6a, 0xdf, 0x92]
f= open('flag.locked_65d0360739a01c5737108cc172ea5c8681249c74', 'rb')
#f = open('test2/important_files/flag.locked', 'rb')
data = f.read()
print data
data_s = data[12:]
blocks =  [data_s[i:i+4] for i in range(0, len(data_s), 4)]

init = 0x5e31bc3
r = ""
for b in blocks:
    res = do16(int(b[::-1].encode('hex'), 16), init)
    init = int(b[::-1].encode('hex'), 16)
    r+= struct.pack("<I", res)
    print hex(res)

open('answer', 'wb').write(r)
print r
