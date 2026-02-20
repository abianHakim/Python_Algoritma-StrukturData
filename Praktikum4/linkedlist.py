#==================================================
# Nama  : Ahmad Abian Hakim
# NIM   : J0403251069
# Kelas : A2
#==================================================

#==================================================
#Implementasi Dasar : Node pada Linked List
#==================================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data  # menyimpan data atau nilai
        self.next = None  # pointer ini untuk menunjuk ke node berikutnya
        
# 1) membuat node dengan instansiasi class Node

nodeA = Node('A')  
nodeB = Node('B')  
nodeC = Node('C')  

# 2) menghubungkan node-node A -> B -> C -> None

head = nodeA  
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Traversal : menelusuri node dari head sampai ke none
current = head 
while current is not None:
    print(current.data)  # meanmpilkan data pada node saat ini
    current = current.next  # pindah ke node berikutnya


#==================================================
# Implementasi Dasar : Stack
#==================================================

