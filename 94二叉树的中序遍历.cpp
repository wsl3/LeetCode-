#include<iostream>
#include<vector>
using namespace std;



struct TreeNode {
    int val;
	TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {} 
};

// 8ms beat 97% ตÝน้
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


int main()
{

	return 0;
}