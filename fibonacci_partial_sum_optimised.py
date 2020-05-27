# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    list1 = [0,1,1]
    for i in range(3,to+3):
        list1.append(list1[i-1]+list1[i-2])
    return((list1[to+2]-list1[from_ + 1])%10)


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))