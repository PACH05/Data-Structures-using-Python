
#Linked List operations

class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
class LL:
    def __init__(self) -> None:
        self.head=None
    def insertbeg(self, data):
       nod = Node(data, self.head)
       self.head=nod
    def printll(self):
       if self.head is None:
           print("List is Empty")
           return 
       else:
        itr = self.head
        lstr = " "
        while itr:
              lstr += str(itr.data) + '-->'
              itr=itr.next
       print(lstr)

    def insertend(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next = Node(data,None)


l=LL()
l.insertbeg(5)
l.insertbeg(7)
l.insertend(9)
l.printll()



