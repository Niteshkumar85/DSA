# Add Last in Linkedlist

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def PrintLl(self):
        if self.head is None:
            print("LinkedList is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data ,"--->",end="")
                n = n.next
    def AddBeg(self,data):
        n_node = Node(data)
        n_node.next = self.head
        self.head = n_node
    def AddEnd(self,data):
        n_node = Node(data)
        if self.head is None:
            self.head = n_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next 
            n.next = n_node

ll = Linkedlist()
ll.AddBeg(10)
ll.AddBeg(20)
ll.AddBeg(30)
ll.AddEnd(50)
ll.PrintLl()
print("\n")