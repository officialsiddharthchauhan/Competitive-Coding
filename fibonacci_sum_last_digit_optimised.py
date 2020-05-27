# # cook your dish here
# # Uses python3

import sys

def get_fibonacci_huge_fast(n):
    list1=[0,1,1]
    for i in range(3,n+3):
        list1.append(list1[i-1]+list1[i-2])
        
    return((list1[-1]-1)%10)
        


if __name__ == '__main__':
    input = sys.stdin.read();
    n = int(input)
    print(get_fibonacci_huge_fast(n))



