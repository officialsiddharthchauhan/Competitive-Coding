# cook your dish here
# Uses python3

import sys

def get_fibonacci_huge_fast(n,m):
    list1=[0,1,1]
    for i in range(3,n+1):
        list1.append(list1[i-1]+list1[i-2])
    #print(list1[-1])
    return(list1[-1]%m)
        


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))