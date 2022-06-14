"""
    first occurrence
        [2,3,4,5,5,6,6,6,7,8,8,8,9] , 6 => 5

"""

def first_occurrence(list_, num):
    for x in range(len(list_)):
        if list_[x] == num :
            return x
    return None


#################################

the_list = [2,3,4,5,5,6,6,6,7,8,8,8,9]
num = 6
result = first_occurrence(the_list, num)
print(result)

