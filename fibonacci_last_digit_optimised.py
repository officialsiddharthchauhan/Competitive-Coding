# cook your dish here
import sys


def f_last(n):
    last_digit=[0,1,1]
    t1=0
    t2=1 
    nextnumber=1
    for _ in range(3,60):
        t1 = t2
        t2=nextnumber
        nextnumber = t1+t2
        last_digit.append(nextnumber%10)
        
    res_index = n%60
    return last_digit[res_index]



'''def period(b):
    for i in range(1, b*b+1):
        if f(i)%b == 0 and f(i+1)%b == 1:
            return(i)
    function to find the periods of particular base last digit repetition 
    
   '''         
            
            

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    #assert(get_fibonacci_last_digit_naive(n)!=f_last(n))
    print(f_last(n))
    #print(get_fibonacci_last_digit_naive(n))
    
        
