#==================================================
# Nama  : Ahmad Abian Hakim
# NIM   : J0403251069
# Kelas : A2
#==================================================

#==================================================
# Implementasi Dasar : Stack
#==================================================

class Node:
      #konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
      def __init__(self, data):
            self.data = data  # menyimpan data atau nilai
            self.next = None  # pointer ini untuk menunjuk ke node berikutnya


# stack ada operasi push(memasukan head baru) dan pop(menghapus head)
# A -> B -> C -> None

class Stack:
    def __init__(self):
            self.top = None # top menuju ke node paling atas (awalnya kosong)

    def push(self, data):
        # 1. membuat node baru
            Nodebaru = Node(data) # instansiasi konstuktor pada  class node
        
        # 2. Node baru merujuk ke top yang lama 
            Nodebaru.next = self.top # node baru menunjuk ke top yang lama

        # 3. GESER TOP KE NODE BARU
            self.top = Nodebaru # top sekarang menunjuk ke node baru


    def tampilkan(self):
            current = self.top # mulai dari top
            print(" Top", end="-> ")
            while current is not None:
                print(current.data, end="-> ") # tampilkan data pada node saat ini
                current = current.next # pindah ke node berikutnya
            print("None") # akhir dari stack

# instansiasi stack
s = Stack()
s.push('A ')
s.push('B ')
s.push('C ')

s.tampilkan() # Output: Top -> A -> None