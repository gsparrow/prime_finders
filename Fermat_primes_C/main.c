#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <iostream>
using namespace std;

int main()
{
  const double ABSOLUTE_MIN=3.0;
  const double MIN=3.0;
  const double MAX=pow(2.0, 63.0);
  const double EVEN=2.0;
  double i;
  double j;
  double J_MAX;
  bool flag;
  #pragma omp for
  for (i=MIN; i<=MAX; i=i+2.0)
  {
    if((((i/EVEN)-(floor(i/EVEN)))*EVEN)==0)
    {
      continue;
    }
    flag=true;
    J_MAX=floor(i/EVEN)+1;
    for(j=ABSOLUTE_MIN; j<=J_MAX; j++)
    {
      if ((((i/j)-(floor(i/j)))*j)==0)
      {
        flag=false;
        j=J_MAX;
      }
    }
    if (flag)
    {
      cout << fixed << std::setprecision(0) << i <<",\n";
    }
  }
}
