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

    def insertAtStart(self,newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    def insertatbetween(self,middle,newdata):

        if middle is None:
            print("Input Correct Data")
            return
        else:
            newnode = Node(newdata)
            newnode.next = middle.next
            middle.next= newnode

    def insertionAtLast(self, newData):
        NewNode = Node(newData)
        if self.head == None:
            self.head = NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = NewNode



lst4 = Root()
lst4.head = Node("Cricket")
second = Node("Volleyball")
third = Node("Basketball")
fourth = Node("Boxing")

lst4.head.next = second
second.next = third
third.next=fourth

lst4.insertAtStart("Suresh")
lst4.insertatbetween(lst4.head.next,"Hockey")
lst4.insertionAtLast("Athidi")