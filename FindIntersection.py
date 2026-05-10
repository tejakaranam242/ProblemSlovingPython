class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class FindIntersection:
    def intersectPoint(self, head1, head2):
        p1 = head1
        p2 = head2
        while(p1!=p2):
            p1 = (head2 if p1==None else p1.next)
            p2 = (head1 if p2==None else p2.next)
        return p1
n = int(input())
value = int(input())
head1 = Node(value)
temp = head1
for i in range(1,n):
    value = int(input())
    newNode = Node(value)
    temp.next=newNode
    temp = newNode
obj = FindIntersection()
result = obj.intersectPoint()
print(result)