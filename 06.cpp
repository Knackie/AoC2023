#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main()
{
	vector <int> nbz;
	vector <int> nbu;
	vector <int> number;
	int forward = 0;
	int depth = 0;
	string finalnb = "";
	vector <int> win;
	win.push_back(0);
	win.push_back(0);
	win.push_back(0);
	win.push_back(0);
	std::fstream fichier("input.txt", std::ios_base::in);

	float a;
	while (fichier >> a)
	{
		number.push_back(a);
	}
	for (int j = 0; j <= 3; j++)
	{
		for (int i = 0; i < number[j]; i++)
		{
			cout << (number[j] - i) * i << "\t";
			if ((number[j] - i) * i > (number[j+4]))
			{
				cout << number[j+4] << endl;
				win[j]++;
			}
		}

	}
	cout << "win : " << win[0] << " " << win[1] << " " << win[2] << " " << win[3] << endl;;
	cout << win[0] * win[1] * win[2] * win[3] << endl;
	return 0;
}

