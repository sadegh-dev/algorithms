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


def alphabet_3bits():
    import string
    alphabet_list = list(string.ascii_lowercase)
    result = list()
    for alp in alphabet_list:
        the_bits = create_3bits()
        result.append(list([alp, the_bits]))
    return result


###### one_timepad_cipher ###########

def do_(char_, key_):
    the_bits = list_alphabet_3bits[char_][1]
    for cc,kk in zip(the_bits, key_):
        if cc == '0' and kk == '0' :
            return '0'
        elif cc == '1' and kk == '0' :
            return '1'
        elif cc == '0' and kk == '1' :
            return '1'
        elif cc == '1' and kk == '1' :
            return '0'


def cipher_(txt_):
    keys_ = list()
    result =''
    for tt in txt_ :
        the_key = create_3bits()
        result += do_(tt,the_key)
        keys_.append(the_key)


    return (list(keys_, result))


def decrypt_(keys_, cipher_txt):
    pass


##################################


list_alphabet_3bits = alphabet_3bits() 



