"""
    search range
        [5,7,7,8,8,8,10], 8  => [3,5]
        [5,7,7,8,8,8,10], 11 => [None,None]

"""

def search_range(list_,num):
    result = list()
    ll = len(list_)
    for x in range(ll):
        if list_[x] == num :
            result.append(x)
    if len(result) == 0 :
        return [None, None]
    else : 
        list_result = list()
        list_result.append(result[0])
        list_result.append(result[-1])
        return list_result



################################


result = search_range([5,7,7,8,8,8,10],8)
print(result)

result = search_range([5,7,7,8,8,8,10],11)
print(result)
