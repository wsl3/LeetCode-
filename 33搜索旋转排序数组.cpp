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
		//�鿴�Ƿ�������
		if (nums[i] < nums[j])
		{
			//����������ô�ͳ���ֲ���
			if (nums[mid] < target) {
				return helper(nums, target, mid + 1, j);
			}
			else {
				return helper(nums, target, i, j - 1);
			}
		}
		else
		{
			//����������i��mid-1���ң����û���ҵ�����mid+1��j����
			int res = helper(nums, target, i, mid - 1);
			return res != -1 ? res : helper(nums, target, mid + 1, j);
		}
	}
};


int main()
{

	return 0;
}