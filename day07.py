#!/bin/python3
"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa',
'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def decode_string(e, k):
    
    # base case, no more digits left besides the one
    if k == 0:
        return 1
    
    # check for next digit == 0 -- non decodable as it's part of either '10'
    # or '20'
    d = len(e) - k
    if e[d] == '0':
        return 0

    # in any case, one digit is a valid character
    ways = decode_string(e, k - 1)

    # depending on the next two digits, it can be a valid character es well
    # if the numeric value is <= 26; also take care for rest string length
    if k >=2 and int(e[d:d+1]) <= 26:
        ways += decode_string(e, k - 2)
        
    return ways

def encode_string(s):
    e = ''
    
    for i in range(len(s)):
        e += str(ord(s[i]) - 96)
    return e

if __name__ == '__main__':
    # create a teststring
    teststring = "thisisaneasytest"
    #teststring = "ak"
    #teststring = "ka"
    #teststring = "aaa"
    
    # encode and print the teststring
    enc = encode_string(teststring)
    print(teststring, ' - ', enc)
    
    # decode the encoded string again and retrieve all 
    # possible strings
    print('Decoding ways: ', decode_string(enc, len(enc)))