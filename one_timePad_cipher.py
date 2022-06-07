"""

    26 letters -> [ a,b,c,d,e,f,...,z ]
    plaintext -> [ 26 of random 3-bits-number ]

    key = [ 3-bits-number for each letter ] 

    ciphertext = [ plaintext (operation) key ]


"""

from random import choice

def create_3bits():
    bits = [0,1]
    result = str(choice(bits))
    for x in range(2):
        result += str(choice(bits))
    return result



