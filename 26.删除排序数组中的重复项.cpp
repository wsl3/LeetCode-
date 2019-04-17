#include<iostream>
#include<string>
#include<vector>
using namespace std;


class Solution {
public:
	int removeDuplicates(vector<int>& nums) {
		if (nums.size() == 0)
		{
			return 0;
		}
		auto i = 0;
		auto j = 1;

		while (j < nums.size())
		{
			if (nums[i] == nums[j])
			{
				j++;
			}
			else
			{
				nums[++i] = nums[j++];
			}
		}
		return i + 1;
		
	}
};

int main()
{
	string temp;
	vector<int> nums = vector<int>(0);
	cout << nums.size();
	Solution s = Solution();
	cout << s.removeDuplicates(nums);

	cin >> temp;
	return 0;
}