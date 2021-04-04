#!/bin/python3
"""
Run-length encoding is a fast and simple method of encoding strings. The basic 
idea is to represent repeated successive characters as a single count and
character. For example, the string "AAAABBBCCDAA" would be encoded as
"4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be
encoded have no digits and consists solely of alphabetic characters. You can
assume the string to be decoded is valid.
"""
def encode(s):
    if not s:
        return ''

    enc = ''
    
    # keep track of the encoded char and how often it appears
    cur_c = ''
    cur_c_ctr = 0

    for c in s:
        # changing char -> write part to encoded string
        if c != cur_c:
            if cur_c != '':
                enc += str(cur_c_ctr) + cur_c

            cur_c = c
            cur_c_ctr = 0
            
        cur_c_ctr += 1
        
    # append the last data
    enc += str(cur_c_ctr) + cur_c
    
    return enc
            

def decode(s):
    dec = ''
    
    # keep track of how many of the following chars will be inserted
    cur_c_ctr = ''
    
    for c in s:
        o = ord(c)
        if o < ord('0') or o > ord('9'):
            # append the character based on the numer of occurenced
            dec += int(cur_c_ctr) * c
            cur_c_ctr = ''
        else:
            cur_c_ctr += c
            
    return dec
        

if __name__ == '__main__':
    s = 'AAAABBBCCDAA'
    
    encoded = encode(s)
    print(encoded)
    
    decoded = decode(encoded)
    print(decoded)