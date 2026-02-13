# Latihan 5: Reverse Single Linked List

class Node:
    def __init__(self, data):
        self.data = data      
        self.next = None      


class LinkedList:
    def __init__(self):
        self.head = None      
        self.tail = None      

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # LATIHAN 5
    def reverse(self):
        prev = None                
        current = self.head        
        self.tail = self.head      

        while current:
            next_node = current.next   
            current.next = prev        
            prev = current            
            current = next_node       

        self.head = prev           


ll = LinkedList()

ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_end(5)

print("Sebelum dibalik:")
ll.display()

ll.reverse()

print("Setelah dibalik:")
ll.display()
