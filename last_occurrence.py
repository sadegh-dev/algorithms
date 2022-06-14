"""
    last occurrence
        [2,3,4,5,5,6,6,6,7,8,8,8,9] , 6 => 7

"""

def last_occurrence(list_, num) :
    ll = len(list_)
    for x in range(ll-1,-1,-1):
        if list_[x] == num :
            return x
    return None


############################


the_list = [2,3,4,5,5,6,6,6,7,8,8,8,9]
num = 6

result = last_occurrence(the_list, num)
print(result)

