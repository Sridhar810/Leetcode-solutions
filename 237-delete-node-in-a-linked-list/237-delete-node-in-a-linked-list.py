# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next==None:
            del node
        node.val,node.next.val=node.next.val,node.val
        temp=node.next
        node.next=node.next.next
        del temp
        