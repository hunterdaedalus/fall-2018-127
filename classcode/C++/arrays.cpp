#include <iostream>

int main()
{
  int a=100;
  int b[4];
  int c=200;
  int i;
  a = 20;
  for (i = 0; i < 4; ++i) {
    b[i]=10*i;
  }

  for (i = 0; i < 4; ++i) {
    std::cout << b[i] << " ";
  }
  std::cout << "\n";
  std::cout << "a: " << a << " c: " << c << "\n";

    b[-1] = 500;
          b[-2] = 600;
      
      
for (i = 0; i < 4; ++i) {
    std::cout << b[i] << " ";
  }
  std::cout << "\n";
  std::cout << "a: " << a << " c: " << c << "\n";
  
  return 0;
}
