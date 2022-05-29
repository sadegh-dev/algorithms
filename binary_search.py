"""
Log2(N)

"""
# None recursive fucntion
def binary_search(the_list, value):
    left_edge , right_edge = 0 , len(the_list) -1
    while left_edge <= right_edge:
        middle = left_edge + (right_edge) -1
        if the_list[middle] == value :
            return middle
        elif the_list[middle] < value :
            left_edge = middle +1
        else :
            right_edge = middle -1
    
    return -1
        
#######################
a_list = [10,20,30,40,50,60,70,80,90]
value = 65
######################

result = binary_search(a_list, value)

print(result)