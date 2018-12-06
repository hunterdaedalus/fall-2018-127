#include <iostream>

int main()
{
  std::string s = "Hello";
  std::cout << s << "\n";
  s = s + s;
  std::cout << s << "\n";

  std::string s2;

  /* This is problematic since >> prases on whitespace
    std::cin >> s2;
  std::cout << s2 << "\n";
  int i;
      std::cin >> i;
  std::cout << i << "\n";
  */

  getline(std::cin,s2);
  std::cout << s2 << "\n";
  std::cout << s2.length() << "\n";

  int i = 0;
  while (i < s2.length()){
    std::cout << s2[i] << "_";
    i++;
  }
    std::cout << "\n";
  s2[8]='X'; // VERY DANGEROUS  you can be off the end of the string
  std::cout << s2 << "\n";

  for (i = 0; i < s2.length(); ++i) {
    std::cout << s2[i] << "-";
  }
  std::cout << "\n";

for (int j = 0; j < 10; j++) {
    std::cout << j << "\n";
 }
/* j only exists in the loop
   so this won't work
std::cout << j << "\n";
*/
  
/*
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


  if (b1) {

  } else if (b2) {

  } else if (b3) {

  } else {

  }
  */
  return 0;
}
