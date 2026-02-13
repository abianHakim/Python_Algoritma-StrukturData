# Latihan 3: Pencarian pada Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data     
        self.next = None      
        self.prev = None      


class DoublyLinkedList:
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
            new_node.prev = self.tail   
            self.tail = new_node        

    def display_forward(self):
        temp = self.head              
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # LATIHAN 3
    def search(self, key):
        temp = self.head             

        while temp:                   
            if temp.data == key:      
                return True
            temp = temp.next         

        return False                 


dll = DoublyLinkedList()

dll.insert_at_end(2)
dll.insert_at_end(6)
dll.insert_at_end(9)
dll.insert_at_end(14)
dll.insert_at_end(20)

print("Isi Doubly Linked List:")
dll.display_forward()

mencari = 9

if dll.search(mencari):
    print("Elemen", mencari, "ditemukan dalam Doubly Linked List.")
else:
    print("Elemen", mencari, "tidak ditemukan dalam Doubly Linked List.")