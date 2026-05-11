class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class ReverseGroupLL:
    def reverseLL(self, head):
        if head == None or head.next == None:
            return head
        newHead = self.reverseLL(head.next)
        front = head.next
        front.next = head
        head.next = None
        return newHead
    def findKthNode(self, head, k):
        k -= 1
        while head != None and k > 0:
            head = head.next
            k -= 1
        return head
    def reverseKGroup(self, head, k):
        temp = head
        previous = None
        while temp != None:
            kthNode = self.findKthNode(temp, k)
            if kthNode == None:
                newHead = self.reverseLL(temp)
                if previous == None:
                    head = newHead
                else:
                    previous.next = newHead
                break
            nextNode = kthNode.next
            kthNode.next = None
            newHead = self.reverseLL(temp)
            if temp == head:
                head = newHead
            else:
                previous.next = newHead
            temp.next = nextNode
            previous = temp
            temp = nextNode
        return head
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
obj = ReverseGroupLL()
result = obj.reverseKGroup(head,k)
print(result)