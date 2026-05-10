class KthNodeFromlast:
    def getKthFromLast(self, head, k):
        slow = head
        fast = head
        for i in range(k):
            if fast == None:
                return -1
            fast = fast.next
        while fast!=None:
            slow = slow.next
            fast = fast.next
        return slow.data
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
n = int(input())
value = int(input())
head = Node(value)
temp = head
for i in range(1,n):
    value = int(input())
    newNode = Node(value)
    temp.next=newNode
    temp = newNode
k = int(input())
obj = KthNodeFromlast()
result = obj.getKthFromLast(head, k)
print(result)