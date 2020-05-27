# Uses python3
import sys

def gcd(a, b):
    if(a==0 or b==0):
        return max(a,b)
    else:
        if(max(a,b)%min(a,b) == 0):
            return min(a,b)
        else:
            return(gcd(min(a,b),max(a,b)%min(a,b)))




def lcm_naive(a,b):
    lcm = int((a*b)/gcd(a,b))
    return lcm

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    #print(gcd(a,b))
    print(lcm_naive(a, b))

