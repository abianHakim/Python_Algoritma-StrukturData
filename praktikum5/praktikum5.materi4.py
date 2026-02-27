# ==========================================================
# Contoh Backtracking 1: Kombinasi Biner (n)
# ==========================================================

def biner(n, hasil=""):  # fungsi backtracking untuk kombinasi biner
    # Base case: jika panjang string sudah samadengan n, cetak hasil
    if len(hasil) == n:  # jika panjang hasil sudah sama dengan n
        print(hasil)  # tampilkan kombinasi
        return  # hentikan cabang ini

    # Choose + Explore: tambah '0'
    biner(n, hasil + "0")  # panggil fungsi dengan menambahkan 0

    # Choose + Explore: tambah '1'
    biner(n, hasil + "1")  # panggil fungsi dengan menambahkan 1

biner(3)  # menghasilkan kombinasi biner sepanjang 3 digit