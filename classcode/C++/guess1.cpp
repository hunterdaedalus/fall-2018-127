#include <iostream>

#include <cstdlib>
#include <ctime>

int main()
{
  // establish the computers number
  srand(time(NULL));
  int answer = rand()%100;

  int guess;

  // repeat until the answer is guessed
  //     get a guess from the user
  //     see if the guess is too low/high/just right
  std::cout << answer << "\n";
  std::cout << "Please enter a guess: ";
  std::cin >> guess;
  int guesses = 1;
  while (guess != answer){
    if (guess > answer) {
      std::cout << "You guessed too high\n";
    } else if (guess < answer){
      std::cout << "You guessed too low\n";
    }
    
    std::cout << "Please enter a guess: ";
    std::cin >> guess;
    guesses++;
  }
  
  std::cout << "Congratulations, you guessed the number!!!\n";
  std::cout << "It took you " << guesses << " guesses.\n";
  return 0;
}
