# Uses python3
from sys import stdin

def fast(n):
    sum1 = 0
    list1=[0,1,1]
    for i in range(3,2*n+1):
        list1.append(list1[i-1]+list1[i-2])
    
    if(n%2==0):
        sum1 = sum(list1[1:2*n-2:4]) + list1[n]**2
        #print(list1[1:2*n-2:4])
    else:
        sum1 = sum(list1[1:2*n+2:4])
        #print(list1[1:2*n+2:4])
    
    return sum1
    
    
if __name__ == '__main__':
    n = int(stdin.read())
    print(fast(n))
