import random
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class FindFirstInLoopInLL:
    def cycleStart(self, head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow.data
        return -1
n = int(input())
value = int(input())
head = Node(value)
temp = head
randomIndex = random.randint(0, n - 1)
loopNode = None
if randomIndex == 0:
    loopNode = head
for i in range(1,n):
    value = int(input())
    newNode = Node(value)
    temp.next=newNode
    temp = newNode
    if i == randomIndex:
        loopNode = newNode
temp.next = loopNode
obj = FindFirstInLoopInLL()
print(obj.cycleStart(head))