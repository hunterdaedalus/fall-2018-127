#include <iostream>

#include <cstdlib>
#include <ctime>

int main()
{
  srand(time(NULL));
  int answer = rand()%100;

  int guesses=0;
  int guess = answer-1;
  
  std::cout << answer << std::endl;
  while (guess != answer){
    std::cout << "Please enter a guess: ";
    std::cin >> guess;
    guesses++;

    if (guess > answer) {
      std::cout << "You guessed too high\n";
    } else if (guess < answer){
      std::cout << "You guessed too low\n";
    }
    
    }
  
  std::cout << "Congratulations, you guessed the number!!!\n";
  std::cout << "It took you " << guesses << " guesses.\n";
  return 0;
}
