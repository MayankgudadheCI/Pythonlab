#include <iostream>
using namespace std;

int
main ()
{

  int N;
  cin >> N;

  for (; N > 0; N--)
    {

      int a, b, c;
      cin >> a >> b >> c;

      if (a == b && a > c)
	cout << c;

      else if (a == b && a < c)
	cout << a;

      else if (c == b && c > a)
	cout << a;

      else if (c == b && c < a)
	cout << c;

      else if (a > b && a < c)
	cout << a;

      else if (a > b && a > c)
	{
	  if (b > c)
	    cout << b;

	  else
	    cout << c;
	}

      else if (b > a && b < c)
	cout << b;

      else if (b > a && b > c)
	{
	  if (a > c)
	    cout << a;

	  else
	    cout << c;
	}
	
	cout<<endl;

    }
    
	return 0;
}
