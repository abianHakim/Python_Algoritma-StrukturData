#==================================================
# Nama : Ahmad Abian Hakim
# NIM : J0403251069
# Kelas : A2
#==================================================

#==================================================
#Implementasi Dasar : Node pada Linked List
#==================================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self, data):
        data.data = data  # menyimpan data atau nilai
        data.next = None  # pointer ini untuk menunjuk ke node berikutnya