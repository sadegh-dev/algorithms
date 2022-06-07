"""

    26 letters -> [ a,b,c,d,e,f,...,z ]
    plaintext -> [ 26 of random 3-bits-number ]

    key = [ 3-bits-number for each letter ] 

    ciphertext = [ plaintext (operation) key ]



'string' -> [101,001,...]
-> +* key[001,101,...]
-> 'new_string'



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
    result = dict()
    for alp in alphabet_list:
        the_bits = create_3bits()
        result.setdefault(alp, the_bits)
    # Return dictionary
    return result


def string_to_3bits(txt, dict):
    result = list()
    for tt in txt :
        result.append(dict[tt])
    return result


def bits3_to_string(bits, dict_):
    result = ''
    for bi in bits :
        for ky,vl in dict_.items() :
            if vl == bi :
                result += ky
                break
    print(result)
    return result


def create_keys(txt):
    result = list()
    for x in range(len(txt)):
        result.append(create_3bits())
    return result



###### one_timepad_cipher ###########

def do_(str_bits, keys_):
    print(str_bits)
    print(keys_)
    result = list()
    for cc,kk in zip(str_bits, keys_):
        result_bits = ''
        for x in range(3) :
            if cc[x] == '0' and kk[x] == '0' :
                result_bits += '0'
            elif cc[x] == '1' and kk[x] == '0' :
                result_bits += '1'
            elif cc[x] == '0' and kk[x] == '1' :
                result_bits += '1'
            elif cc[x] == '1' and kk[x] == '1' :
                result_bits += '0'
        result.append(result_bits)
    print(result)
    return result



def cipher_(txt, list_alphabet_3bits):
    # text to
    str_3bits = string_to_3bits(txt, list_alphabet_3bits)
    the_keys = create_keys(txt)
    new_3bits = do_(str_3bits, the_keys)
    new_txt = bits3_to_string(new_3bits, list_alphabet_3bits)

    # txt_cipher = { 'new_txt' : value , 'keys' : list of keys}
    result = dict()
    result.setdefault('new_txt', new_txt)
    result.setdefault('the_keys', the_keys)
    print(result)
    return result




def decrypt_(keys_, cipher_txt):
    pass


##################################

# Create 26 3bits for alphabet
list_alphabet_3bits = alphabet_3bits() 


txt = "hello"

text_cipher = cipher_(txt, list_alphabet_3bits)



