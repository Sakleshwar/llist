class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def insertionAtLast(self, newData):
        NewNode = Node(newData)
        if self.head == None:
            self.head = NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = NewNode


lst2 = LinkedList()
lst2.head = Node("Srinivasan")
second = Node("Suresh")
third = Node("Saklesh")

lst2.head.next = second
second.next = third

lst2.insertionAtLast("Vamshi")


