#include <iostream>

#include <cstdlib>
#include <ctime>

int main()
{
  
  int guesses=0;
  int guess = 50;
  int isCorrect;
  
  std::cout << "I'm guessing: " << guess << "\n";
  std::cout << "0 = right, -1 = too low, 1 = too high\n";
  std::cin >> isCorrect;
  while (isCorrect != 0){
    

    if (isCorrect == -1) {
      guess = guess + (100 - guess)/2;
    } else if (isCorrect == 1){
      guess = guess - (guess / 2) ;
    }
    std::cout << "I'm guessing: " << guess << "\n";
    std::cout << "0 = right, -1 = too low, 1 = too high\n";
    std::cin >> isCorrect;
    guesses ++;
    }
  
  std::cout << "It took me " << guesses << " guesses.\n";
  return 0;
}
