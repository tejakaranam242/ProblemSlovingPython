class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class ReverseLL:
    def reverseList(self, head):
        if head == None or head.next==None:
            return head
        newHead = self.reverseList(head.next)
        front = head.next
        front.next = head
        head.next = None
        return newHead
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
obj = ReverseLL()
result = obj.reverseList(head)
print(result)