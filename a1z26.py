

def encode_ (string_):
    result = list()
    for x in string_:
        result.append(ord(x))
    return result


def decode_q (coding):
    result = ""
    for x in coding :
        result += chr(x)
    return result



txt = 'hello world !'
result = encode_(txt)
print(result)

result_txt = decode_q(result)
print(result_txt)
