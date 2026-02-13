# Latihan 3: Pencarian pada Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data     
        self.next = None      # Pointer ke node berikutnya
        self.prev = None      # Pointer ke node sebelumnya


class DoublyLinkedList:
    def __init__(self):
        self.head = None      # Node pertama
        self.tail = None      # Node terakhir

    def insert_at_end(self, data):
        new_node = Node(data)     # Buat node baru

        if not self.head:         # Jika kosong
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node   # Sambungkan node terakhir ke node baru
            new_node.prev = self.tail   # Hubungkan kembali ke belakang
            self.tail = new_node        # Update tail

    def display_forward(self):
        temp = self.head              # Mulai dari head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # LATIHAN 3
    def search(self, key):
        temp = self.head              # Mulai dari head

        while temp:                   # Selama masih ada node
            if temp.data == key:      # Jika data ditemukan
                return True
            temp = temp.next          # Pindah ke node berikutnya

        return False                  # Jika tidak ditemukan


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