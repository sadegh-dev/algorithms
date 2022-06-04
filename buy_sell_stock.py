"""
    buy - sell stock

    [2, 6, 7, 4, 3, 2, 8] ->

"""

def buy_sell_stock(arr):
    statics_ = dict()
    for p, x in enumerate(arr[1:]) :
        diff_ = x -arr[p-1]
        print(diff_) 


arr = [2, 6, 7, 4, 3, 2, 8]

buy_sell_stock(arr)

#print(result)

