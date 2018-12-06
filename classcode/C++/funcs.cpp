#include <iostream>

int add2(int a, int b) ;

int add4(int a, int b, int c, int d){
  int x = add2(a,b);
  int y = add2(c,d);
  return add2(x,y);
}


int add2(int a, int b){
  int c;
  c = a + b;
  return c;
}




std::string times(std::string s, int t){
  std::string result = "";
  for (int i = 0; i < t; ++i) {
    result = result + s;
  }
  return result;

}

void printGreeting(std::string name){
  std::cout << "Hello " << name <<"\n";
  return;  // this just goes back to the caller, doesn't send back a value
}

int fact(int n){
  int product = 1;
  for (int i = n ; i > 1; i--){
    product = product * i;
  }
  return product;
}
int main()
{
  int a=10, b = 20;
  int x = add2(a,b);
  std::cout << x << "\n";
  x = add2(100,500);
  std::cout << x << "\n";

  std::cout << add2(100.5,300)<< "\n"; // note how this truncates our result
  std::cout << times("Heloo_",5) << "\n";

  printGreeting("Stan");

  std::cout << add4(1,2,10,20) << "\n";

  std::cout << fact(4) << "\n";
  return 0;
}
