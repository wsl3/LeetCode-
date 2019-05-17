#include<iostream>
using namespace std;




struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// 8ms beat 97.8%
// Ë«Ö¸Õë, Ò»´ÎÉ¨Ãè
class Solution {
public:
	ListNode* removeNthFromEnd(ListNode* head, int n) {
		auto res = new ListNode(-1);
		res->next = head;
		if (head == nullptr || n == 0)
		{
			return head;
		}

		auto left = res, right = head;
		while (n != 0)
		{
			right = right->next;
			n--;
		}
		while (right != nullptr)
		{
			right = right->next;
			left = left->next;
		}
		left->next = left->next->next;
		return res->next;
	}
};


int main()
{

	return 0;
}