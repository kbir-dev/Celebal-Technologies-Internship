#Create a Python program that implements a singly linked list using Object-Oriented Programming (OOP) principles. Your implementation should include the following: A Node class to represent each node in the list. A LinkedList class to manage the nodes, with methods to: Add a node to the end of the list Print the list Delete the nth node (where n is a 1-based index) Include exception handling to manage edge cases such as: Deleting a node from an empty list Deleting a node with an index out of range Test your implementation with at least one sample list.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_node(self,data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.tail.next = new_node
        self.tail = new_node
        
    def delete_nth_node(self, n):
     if self.head is None:
         raise Exception("List is empty. Nothing to delete.")
     
     if n == 1:
         self.head = self.head.next
         if self.head is None:
             self.tail = None
         return
     
     temp = self.head
     for i in range(n - 2):
         if temp is None or temp.next is None:
             raise IndexError("Index out of bounds")
         temp = temp.next
 
     if temp.next is None:
         raise IndexError("Index out of bounds")
     
     if temp.next == self.tail:
         self.tail = temp
     
     temp.next = temp.next.next
            
                
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=' -> ')
            temp = temp.next
        print("None")
        
def main():
    ll = LinkedList()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(4)
    ll.add_node(5)
    ll.print_list()           
    ll.delete_nth_node(3)
    ll.print_list()           
    ll.delete_nth_node(1)
    ll.print_list() 
    
main()