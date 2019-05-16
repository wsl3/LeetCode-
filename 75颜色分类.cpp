#include<iostream>
#include<vector>
using namespace std;

//beat 95.28%
//����1���ùܣ�����0�ƶ���ǰ�棬����2�ƶ��������
class Solution {
public:
	void sortColors(vector<int>& nums) {
		if (nums.size() == 1)
		{
			return;
		}
		int i = 0, j = 0, k = nums.size()-1;

		while (j <= k)
		{
			if (nums[j] == 0)
			{
				//������nums[j]Ϊ0����1��j�ƶ�����һ��
				swap(nums, i, j);
				i++;
				j++;
			}
			else if (nums[j] == 1)
			{
				//����1���ù�
				j++;
			}
			else if (nums[j] == 2)
			{
				//swap��nums[j]������0,1,2�����ٴ��ж�
				swap(nums, j, k);
				k--;
			}
		}
	
	}
	void swap(vector<int>& nums, int i, int j)
	{
		int temp = nums[i];
		nums[i] = nums[j];
		nums[j] = temp;
	}
};






//12ms beat 47% 
/*
class Solution {
public:
	void sortColors(vector<int>& nums) {
		int count_0 = 0, count_1 = 0, count_2 = 0;
		for (int i = 0; i < nums.size(); i++) 
		{
			if (nums[i] == 0) {
				count_0++;
			}
			else if (nums[i] == 1) {
				count_1++;
			}
			else if (nums[i] == 2) {
				count_2++;
			}
		}
		for (int i = 0; i < count_0; i++)
		{
			nums[i] = 0;
		}
		for (int i = count_0; i < (count_0 + count_1); i++)
		{
			nums[i] = 1;
		}
		for (int i = count_0 + count_1; i < nums.size(); i++)
		{
			nums[i] = 2;
		}
	}
};
*/


int main(int ac, char* av[]) {

	return 0;
}