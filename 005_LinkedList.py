# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:11:41 2024

@author: Lycoris
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def showNodes(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next
            
    def appendAtEnd(self, data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
        
    def deleteFromEnd(self):
        if (self.head == None):
            return "LinkList is Empty"
        
        if (self.head.next == None):
            self.head = None #delete success
            return
        
        temp = self.head
        while(temp.next.next):
            temp = temp.next
        temp.next = None
        
        
links = LinkedList()
links.append(10)
links.append(4)
links.append(9)

links.appendAtEnd(5)
links.showNodes()
print("\n")
links.deleteFromEnd()
links.showNodes()



