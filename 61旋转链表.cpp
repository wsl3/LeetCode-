#include<iostream>
#include<vector>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

//12ms beat 98%
class Solution {
public:
	ListNode* rotateRight(ListNode* head, int k) {
		auto p = head;
		auto count = 0; //链表长度
		while (p != nullptr) { count++; p = p->next; }
		//链表长度为0
		if (count == 0)
		{
			return head;
		}
		//k==count 时不用旋转
		k = k % count;
		if (k == 0)
		{
			return head;
		}
		//移动p指针到 要移动元素的前面
		p = head;
		for (int i = 1; i < count - k; i++)
		{
			p = p->next;
		}
		//移动元素 和 不移动元素脱离
		auto temp_head = p->next;
		p->next = nullptr;
		p = temp_head;

		//旋转并且重新连接
		while (p->next != nullptr) { p = p->next; }
		p->next = head;
		head = temp_head;

		return head;
	}
};


int main(int ac, char* av[]) {

	return 0;
}