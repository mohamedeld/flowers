class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printall(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

    def insert(self,head,data):
        n = Node(data)
        if head:
            current = head
            while current.next:
                current = current.next
            current.next = n
            return head
        else:
            return n

llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)


llist.head.next = second

second.next = third

llist.printall()
llist.insert(llist.head,50)
