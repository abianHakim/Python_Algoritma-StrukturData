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

    def is_empty(self):
            return self.top is None # stack kosong jika top tidak menunjuk ke node manapun (None)


    def pop(self):
            # 1. Periksa apakah stack kosong
            if self.top is None:
                    print("Stack kosong, tidak ada yang bisa dipop.")
                    return None
            data_terhapus = self.top.data # simpan data yang akan dihapus
            self.top = self.top.next # geser top ke node berikutnya (node setelah top yang lama)
            return data_terhapus # kembalikan data yang dihapus

    def peek(self):
        if self.top is None:
            return None
        return self.top.data # kembalikan data pada top tanpa menghapusnya

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
s.tampilkan()
print('peek (lihat top):', s.peek())
s.pop() 
s.tampilkan()
print('peek (lihat top):', s.peek())    
# s.pop() 
# s.tampilkan()
# s.pop() 
# s.tampilkan()
