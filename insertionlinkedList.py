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

    def insertAtStart(self,newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

lst3 = LinkedList()
lst3.head = Node("Veerendera")
second = Node("Nitish")
third = Node("Sai")

lst3.head.next = second
second.next = third


#lst3.insertAtStart("Pavan")

