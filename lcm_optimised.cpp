#include <iostream>
#include<algorithm>
using namespace std;


int gcd(int a, int b)
{
    if(a==0 || b==0)
        return max(a,b);
    else
    {
        if(max(a,b)%min(a,b) == 0)
            return min(a,b);
        else
            return gcd(min(a,b), max(a,b)%min(a,b));
            
    }
}


int  lcm_fast(int a, int b) {
   int lcm = (a*b)/gcd(a,b);
   return lcm;
}







int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout <<lcm_fast(a, b) << std::endl;
  return 0;
}
