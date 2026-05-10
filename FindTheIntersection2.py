import random
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class FindTheIntersection2:
    def intersection(self,head1,head2):
        pointer1 = head1
        pointer2 = head2
        while pointer1!=pointer2:
           pointer1 = (head2 if pointer1==None else pointer1.next)
           pointer2 = (head1 if pointer2 == None else pointer2.next)
        return pointer1.data
n1 = int(input())
n2 = int(input())
value = int(input())
head1 = Node(value)
temp = head1
randomIndex = random.randint(0,n1)
interSectionNode = None
for i in range(1,n1):
    value = int(input())
    newNode = Node(value)
    if(i==randomIndex):
        interSectionNode = newNode
    temp.next = newNode
    temp = newNode
value = int(input())
head2 = Node(value)
temp = head2
for i in range(1,n2):
    value = int(input())
    newNode = Node(value)
    temp.next = newNode
    temp = newNode
temp.next = interSectionNode
obj = FindTheIntersection2()
result = obj.intersection(head1,head2)
print(result)