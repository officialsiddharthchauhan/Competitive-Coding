# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    list1=[0,1,1]
    for i in range(3,n+1):
        list1.append(list1[i-1]+list1[i-2])
    return(list1[-1])
    
n = int(input())
print(calc_fib(n))
