x = 1

def hello(n):
    print(n)
    if(1<n):
        return hello(n-1)


result = hello(5)