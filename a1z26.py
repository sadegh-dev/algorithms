

def encode_ (string_):
    result = list()
    for x in string_:
        result.append(ord(x))
    return result




txt = 'hello world !'
result = encode_(txt)
print(result)
