"""
    rotate
        rotate("yellow",2) return "llowye"
        rotate("yellow",5) return "wyello"
        rotate("yellow",6) return "yellow"
        rotate("yellow",7) return "ellowy" 
"""

def rotate(txt, num):
    ll = len(txt)
    if num > ll :
        num_rotate = num % ll
    else :
        num_rotate = num
    
    the_rotate = txt[:num_rotate]
    newtxt = txt[num_rotate:]
    newtxt = newtxt+the_rotate
    return newtxt


################################


result = rotate("hello",2)
print(result)

result = rotate("katty",17)
print(result)

result = rotate("bye",6)
print(result)


result = rotate("yellow",7)
print(result)


