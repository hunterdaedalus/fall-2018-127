#include <iostream>
#include <cstdlib>
#include <ctime>


int main()
{

  srand(time(NULL));
  
  int x = 1;
  int i;
  for (i = 1; i < 5; i++) {
    x = x * i;
  }
  std::cout << x << "\n";

  x = 1;
  i=1;
  while (i < 5){
    x = x * i;
    i++;
  }

    std::cout << x << "\n";
    int r;
        
    for (r = rand()%100;
	 r != 20 ;
	 r = rand()%100 ) {
      std::cout << r << " ";
          
    }

    
    std::cout << r << "\n";
  return 0;
}
