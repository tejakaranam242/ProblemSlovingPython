class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def printLL(head):
    current = head
    while current!=None:
        print(current.data,end=" ")
        current = current.next
def reverseList(head):
    if head == None or head.next == None:
        return head
    newNode = reverseList(head.next)
    front = head.next
    front.next = head
    head.next = None
    return newNode
def isPalindrome(head):
    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    newNode = reverseList(slow.next)
    first = head
    second = newNode
    while second != None:
        if first.data != second.data:
            reverseList(newNode)
            return False
        first = first.next
        second = second.next
    reverseList(newNode)
    return True
n = int(input())
value = int(input())
head = Node(value)
temp = head
for i in range(1,n):
    value = int(input())
    newNode = Node(value)
    temp.next=newNode
    temp = newNode
printLL(head)
result = isPalindrome(head)
print(result)