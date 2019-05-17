#include<iostream>
#include<vector>
using namespace std;

//8ms beat 98%
class Solution {
public:
	int search(vector<int>& nums, int target) {
		return helper(nums, target, 0, nums.size() - 1);
	}
	int helper(vector<int>& nums, int target, int i, int j)
	{
		if (i > j)
		{
			return -1;
		}
		int mid = (i + j) / 2;
		if (nums[mid] == target)
		{
			return mid;
		}
		//查看是否是升序
		if (nums[i] < nums[j])
		{
			//是升序则采用传统二分查找
			if (nums[mid] < target) {
				return helper(nums, target, mid + 1, j);
			}
			else {
				return helper(nums, target, i, j - 1);
			}
		}
		else
		{
			//非有序，先在i到mid-1查找，如果没有找到就在mid+1到j查找
			int res = helper(nums, target, i, mid - 1);
			return res != -1 ? res : helper(nums, target, mid + 1, j);
		}
	}
};


int main()
{

	return 0;
}