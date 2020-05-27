#include <iostream>
#include <algorithm>
using namespace std;
int gcd_naive(int a, int b) {
  int current_gcd = 1;
  for (int d = 2; d <= a && d <= b; d++) {
    if (a % d == 0 && b % d == 0) {
      if (d > current_gcd) {
        current_gcd = d;
      }
    }
  }
  return current_gcd;
}

int gcd_fast(int a, int b){
    if(a==0 || b==0)
        return max(a,b);
    else
    {
        if(max(a,b)%min(a,b)==0)
            return min(a,b);
        else
            return(gcd_fast(min(a,b),max(a,b)%min(a,b)));
    }
        
}

int main() {
  int a, b;
  std::cin >> a >> b;
  //std::cout <<"Naive ::"<<gcd_naive(a, b) << std::endl;
  cout<<gcd_fast(a,b)<<endl;
  return 0;
}
