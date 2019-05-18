#include<iostream>
#include<vector>
using namespace std;

struct TreeNode {
    int val;
	TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {} 
};

// 0ms beat 100% 基于栈的非递归
class Solution {
public:
	vector<int> inorderTraversal(TreeNode* root) {
		vector<int> res;
		vector<TreeNode*> stack;

		while (root != nullptr || !stack.empty())
		{
			while (root != nullptr)
			{
				stack.push_back(root);
				root = root->left;
			}
			if (!stack.empty())
			{
				root = stack[stack.size()-1];
				stack.pop_back();
				res.push_back(root->val);
				root = root->right;
			}
		}
		return res;
	}
};



// 8ms beat 97% 递归
/*
class Solution {
public:
	vector<int> inorderTraversal(TreeNode* root) {
		vector<int> res;
		helper(res, root);
		return res;
	}

	void helper(vector<int> &res, TreeNode* node)
	{
		if (node == nullptr)
		{
			return;
		}
		helper(res, node->left);
		res.push_back(node->val);
		helper(res, node->right);
	}
};
*/


int main()
{

	return 0;
}