// Last updated: 02/03/2026, 14:03:23
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(); // Dummy head of the result linked list
        ListNode* curr = dummy; // Pointer to traverse the result linked list
        int carry = 0; // Variable to store the carry
        
        while (l1 || l2 || carry) {
            int sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry; // Calculate sum
            
            carry = sum / 10; // Calculate carry for the next iteration
            sum %= 10; // Update sum
            
            curr->next = new ListNode(sum); // Create a new node with the sum
            curr = curr->next; // Move to the next node
            
            // Move to the next node in both linked lists, if they exist
            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
        }
        
        return dummy->next; // Return the next node after the dummy head
    }
};
