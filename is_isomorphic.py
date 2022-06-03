def is_isomorphic(x,y):
    if not (len(x) == len(y)):
        return False

    ref = dict()
    for xx , yy in zip(x,y):
        pos = ref.setdefault(xx,yy)
        if pos != yy :
            return False

    return True


###########################

x = "helloe"
y = "yippqi"

result = is_isomorphic(x,y)

print(result)