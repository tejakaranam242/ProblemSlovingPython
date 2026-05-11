class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def mergeLists(self, list1, list2):
        dummyNode = Node(-1)
        res = dummyNode
        while list1 != None and list2 != None:
            if list1.data < list2.data:
                res.bottom = list1
                res = list1
                list1 = list1.bottom
            else:
                res.bottom = list2
                res = list2
                list2 = list2.bottom
            res.next = None
        if list1 != None:
            res.bottom = list1
        if list2 != None:
            res.bottom = list2
        return dummyNode.bottom
    def flatten(self, root):
        if root == None or root.next == None:
            return root
        mergedHead = self.flatten(root.next)
        return self.mergeLists(root, mergedHead)