
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

    def InsertBegin(self,data):
        nb=Node(data)
        nb.ref=self.head
        self.head=nb


    def Insertion_at_End(self,data):
        ne=Node(data)
        a=self.head
        while a.ref != None:
            a=a.ref
        a.ref=ne

    def Ins_Specified_Node(self,position,data):
        ns=Node(data)
        a=self.head
        for i in range(1, (position-1)):
            a=a.ref
        ns.ref= a.ref
        a.ref=ns


n1=Node(10)
ll=linkedlist()
ll.head=n1
n2=Node(20)
n1.ref=n2
n3=Node(30)
n2.ref=n3
n4=Node(40)
n3.ref=n4


ll.InsertBegin(0)
ll.Ins_Specified_Node(3,15)
ll.Insertion_at_End(50)
ll.Insertion_at_End(60)

ll.traversal()
