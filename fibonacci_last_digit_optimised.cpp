#include <iostream>
#include<cassert>
using namespace std;

int fast_last(int n) {
        
        
    int arr[60];
    
    arr[0] = 0;
    arr[1] = 1;

    int previous = 0;
    int current  = 1;

    for (int i = 2; i < 60; ++i) {
        int tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
        arr[i] = current%10;
    }
    int res_index = n%60;
    int result = arr[res_index];
    return result;
}

/*int get_fibonacci_last_digit_naive(int n) {
    if (n <= 1)
        return n;

    int previous = 0;
    int current  = 1;

    for (int i = 0; i < n - 1; ++i) {
        int tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % 10;
}
*/


int main() {
    int n;
    std::cin >> n;
    int c = fast_last(n);
    //int d = get_fibonacci_last_digit_naive(n);
    //assert(fast_last(n)==get_fibonacci_last_digit_naive(n));
    //cout<<d<<" - Non optimised"<<"\n";
    std::cout << c;
    
}
