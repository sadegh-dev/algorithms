"""
    rotate
        rotate("yellow",2) return "llowye"
        rotate("yellow",5) return "yellow"
        rotate("yellow",6) return "ellowy"
        rotate("yellow",7) return "llowye" 
"""


def rotate(txt, num):
    ll = len(txt)
    if num > ll :
        num_rotate = num % ll
    else :
        num_rotate = num
    
    the_rotate = txt[:num_rotate]
    newtxt = txt[num_rotate:]




result = rotate("hello",3)
#print(result)

result = rotate("hello",7)
#print(result)


print(7%5)
