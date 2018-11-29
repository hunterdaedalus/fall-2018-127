#include <iostream>

int main()
{
  int i = 20;

  if (i > 10)
    std::cout << "i is greater than 10\n";
  std::cout << "more stuff not in the if statement\n";

  std::cout << "\n\n";
  if (i < 10)
    std::cout << "i is less than 10\n";
  std::cout << "more stuff not in the if statement\n";

  if (i>10){
    std::cout << "i is greater than 10\n";
    std::cout << "with a second statement\n";
  }
  
  if (i<10){
    std::cout << "i is less than 10\n";
    std::cout << "with a second statement\n";
  }


  if (i > 10){
    std::cout << "I is greater with an else\n";
  } else {
    std::cout << "i is less with an else\n";
  }

  /*
  if (b1) {

  } else if (b2) {

  } else if (b3) {

  } else {

  }
  */
  return 0;
}
