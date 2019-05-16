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
		auto count = 0; //������
		while (p != nullptr) { count++; p = p->next; }
		//������Ϊ0
		if (count == 0)
		{
			return head;
		}
		//k==count ʱ������ת
		k = k % count;
		if (k == 0)
		{
			return head;
		}
		//�ƶ�pָ�뵽 Ҫ�ƶ�Ԫ�ص�ǰ��
		p = head;
		for (int i = 1; i < count - k; i++)
		{
			p = p->next;
		}
		//�ƶ�Ԫ�� �� ���ƶ�Ԫ������
		auto temp_head = p->next;
		p->next = nullptr;
		p = temp_head;

		//��ת������������
		while (p->next != nullptr) { p = p->next; }
		p->next = head;
		head = temp_head;

		return head;
	}
};


int main(int ac, char* av[]) {

	return 0;
}