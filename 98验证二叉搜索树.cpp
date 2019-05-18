#include<iostream>
#include<vector>
using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// 12ms beat 97.78%
// 搜索树按照中序遍历后是升序的
class Solution {
public:
	bool isValidBST(TreeNode* root) {
		if (root == nullptr)
		{
			return true;
		}
		vector<int> res;
		helper(res, root);

		for (size_t i = 1; i < res.size(); i++)
		{
			if (res[i] <= res[i - 1])
			{
				return false;
			}
		}
		return true;
	}
	void helper(vector<int> &res, TreeNode* node)
	{
		if (node == nullptr)
		{
			return;
		}
		helper(res,node->left);
		res.push_back(node->val);
		helper(res, node->right);
	}
};

int main()
{

	return 0;
}