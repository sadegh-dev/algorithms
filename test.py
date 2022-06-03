

def is_isomorphic(x,y):
    if not (len(x) == len(y)):
        return False
    
    ref = dict()
    for xx , yy in zip(x,y):
        pos = ref.setdefault(xx,yy)
        if pos != yy :
            return False

    return True


##############################3

x = "helloe"
y = "yipptp"

result = is_isomorphic(x,y)
print(result)





