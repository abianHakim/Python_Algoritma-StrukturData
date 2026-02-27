# ==========================================================
# Contoh Rekursi 2: Tracing Masuk/Keluar
# ==========================================================

def hitung(n): # fungsi rekursif untuk melihat proses masuk dan keluar
    #base case
    if n == 0: #jika n sudah 0
        print("selesai")
        return #hentikan fungsi
    print("Masuk : ",n)     # fase stacking (fungsi masuk ke stack)
    hitung(n -1)            # pemanggilan rekursif dengan n-1
    print("Keluar : ",n)    # fase unwinding (fungsi keluar dari stack)

hitung(3) #Memanggil fungsi dengan nilai awal 3   