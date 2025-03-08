#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def addTwoNumbers(self, l_list_1, l_list_2):
        result_l_list = ListNode(val = None)
        result_node = result_l_list

        dummy_node_1 = ListNode(val = None)
        dummy_node_1.next = l_list_1

        dummy_node_2 = ListNode(val = None)
        dummy_node_2.next = l_list_2

        curr_node_1 = dummy_node_1.next
        curr_node_2 = dummy_node_2.next

        sum_digit = 0
        carry = 0
        while (curr_node_1 is not None or curr_node_2 is not None):
            if (curr_node_1 is not None and curr_node_2 is not None):
                sum_digit = curr_node_1.val + curr_node_2.val + carry
            elif (curr_node_1 is not None):
                sum_digit = curr_node_1.val + carry
            elif (curr_node_2 is not None):
                sum_digit = curr_node_2.val + carry
            carry = sum_digit // 10
            sum_digit = sum_digit % 10
            result_node.next = ListNode(sum_digit)
            result_node = result_node.next

            if (curr_node_1 is not None):
                curr_node_1 = curr_node_1.next
            if (curr_node_2 is not None):
                curr_node_2 = curr_node_2.next
            
        if (carry > 0):
            result_node.next = ListNode(carry)
            result_node = result_node.next

        return result_l_list.next
