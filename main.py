class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class Root:
    def __init__(self):
        self.head = None
    
    def display(self):

        while self.head is not None:
            print(self.head.data)
            self.head = self.head.next

    def insertatbetween(self,middle,newdata):

        if middle is None:
            print("Input Correct Data")
            return
        else:
            newnode = Node(newdata)
            newnode.next = middle.next
            middle.next= newnode




lst = Root()
lst.head = Node("Cricket")
second = Node("Volleyball")
third = Node("Basketball")
fourth = Node("Boxing")

lst.head.next = second
second.next = third
third.next=fourth

lst.insertatbetween(lst.head.next,"Hockey")
lst.display()