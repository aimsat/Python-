class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None


class linkedlist:
    def __init__(self):
        self.head=None

    def traversal(self):
        if self.head==None:
            print("LL is empty")
        else:
            a=self.head
            while a != None:
                print(a.data)
                a=a.ref

n1=Node(10)
ll=linkedlist()
ll.head=n1
n2=Node(20)
n1.ref=n2
n3=Node(30)
n2.ref=n3
n4=Node(40)
n3.ref=n4

ll.traversal()

