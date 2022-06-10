"""
    two sum
    [2, 7, 11, 15] , 22 -> [1,3]

"""


def two_sum(list_, sum):
    result = list()
    ll = len(list_)
    for x in range(ll-1):
        for y in range(1,ll) :
            if list_[x]+list_[y] == sum and x != y :
                result = list((x,y))
                return result

########################

list_a = [2,5,11,15]
sum = 16

result = two_sum(list_a, sum)

print(result)

