"""
    two sum
    [2, 7, 11, 15] , 22 -> [1,3]

"""


def two_sum(list_, sum):
    ll = len(list_)
    for x in range(ll):
        for y in range(ll) :
            if list_[x]+list_[y] == sum and x != y :
                return list((x,y))

########################

list_a = [2,5,11,15,35]
sum = 46

result = two_sum(list_a, sum)

print(result)

