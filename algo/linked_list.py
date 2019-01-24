class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        curNode = self.head
        while(curNode.next != None):
            curNode = curNode.next
        curNode.next = Node(val)

    def printLinkedList(self):
        curNode = self.head
        while(curNode != None):
            print(curNode.val)
            curNode = curNode.next 
list1 = SinglyLinkedList()
list1.head = Node(2)

print(list1.head.val)
