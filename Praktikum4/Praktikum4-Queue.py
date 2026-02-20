#==================================================
# Nama  : Ahmad Abian Hakim
# NIM   : J0403251069
# Kelas : A2
#==================================================

#==================================================
# Implementasi Dasar : Queue
#==================================================

class Node:
      #konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
      def __init__(self, data):
            self.data = data  # menyimpan data atau nilai
            self.next = None  # pointer ini untuk menunjuk ke node berikutnya

class queue:
    #   konstruktor untuk inisialisasi queue dengan front dan rear
    def __init__ (self):
            self.front = None # front menuju ke node paling depan (awalnya kosong)
            self.rear = None # rear menuju ke node paling belakang (awalnya kosong)

    def is_empty(self):
            return self.front is None # queue kosong jika front tidak menunjuk ke node manapun (None)

    # membuat fungsi untuk menambah data baru
    def enqueue(self, data):
        nodebaru = Node(data)

        if self.is_empty(): # jika queue kosong, front dan rear menunjuk ke node baru
            self.front = nodebaru
            self.rear = nodebaru    
        else:
            self.rear.next = nodebaru # rear menunjuk ke node baru
            self.rear = nodebaru # rear sekarang menunjuk ke node baru
        return
    
    def dequeue(self):
        #   menghapus data dari depan queue
        data_terhapus = self.front.data # lihat data uyang di depan
        
        self.front = self.front.next # geser front ke node berikutnya
        if self.front is None:
            self.rear = None # jika queue menjadi kosong, rear juga harus diatur ke None
        return data_terhapus # kembalikan data yang dihapus
             


    def tampilkan(self):
            current = self.front # mulai dari front
            print(" Front ", end="-> ")
            while current is not None:
                print(current.data, end="-> ") # tampilkan data pada node saat ini
                current = current.next # pindah ke node berikutnya
            print("None") # akhir dari queue


q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()

