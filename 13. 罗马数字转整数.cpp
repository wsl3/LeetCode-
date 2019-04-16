#include<iostream>
#include<string>
#include<map>
using namespace std;


class Solution {
public:
	int romanToInt(string s) {
		int length = s.length();
		int num = 0;
		map<char, int> dict;
		dict['I'] = 1;
		dict['V'] = 5;
		dict['X'] = 10;
		dict['L'] = 50;
		dict['C'] = 100;
		dict['D'] = 500;
		dict['M'] = 1000;
		
		for (int i = 0; i < length; i++)
		{
			num += dict[s[i]];
			if (i == 0)
			{
				continue;
			}
			if ((s[i] == 'V' || s[i] == 'X') && s[i-1]=='I') 
			{
				num -= 2;
			}
			else if (((s[i] == 'L' || s[i] == 'C') && s[i - 1] == 'X'))
			{
				num -= 20;
			}
			else if (((s[i] == 'D' || s[i] == 'M') && s[i - 1] == 'C'))
			{
				num -= 200;
			}
		}
		return num;
	}
};

int main()
{
	string temp;
	Solution s = Solution();
	cout << s.romanToInt("IV")<< endl;
	cin >> temp;
	return 0;
}