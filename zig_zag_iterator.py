"""
    zig zag iterator
    [a(0), b(0), a(1), b(1), a(2), b(2), ... ]

    Ex1:
    [10, 30, 90, 110, 70]
    [20, 60, 40, 100, 60]
    => [10, 20, 30, 60, 90, 40, 110, 100, 70, 60]

"""

# Solution1 [ with zip function ] #

def zig_zag_iterator_1(arr1, arr2) :
    result = list()
    for a1,a2 in zip(arr1, arr2):
        result.append(a1)
        result.append(a2)
    
    diff_ = len(arr1) - len(arr2)
    if diff_ > 0 :
        result.extend(arr1[-diff_:])
    elif diff_ < 0 :
        result.extend(arr2[diff_:])
    
    return result


# Solution2 [ without zip function ] #

from copy import deepcopy

def zig_zag_iterator_2(arr1, arr2) :
    result = list()
    diff_ = len(arr1) - len(arr2)
    if diff_ < 0 :
        c = deepcopy(arr1)
        arr1 = deepcopy(arr2)
        arr2 = deepcopy(c)
    
    #always here -> len(arr1) > len(arr2)
    for x in range(len(arr2)) :
        result.append(arr1[x])
        result.append(arr2[x])
    
    if abs(diff_):
        result.extend(arr1[-abs(diff_):])

    return result

####################################

l1 = [10, 30, 90, 66]
l2 = [20, 60, 40, 50,800,900]

result = zig_zag_iterator_2(l1, l2)

print(result)

