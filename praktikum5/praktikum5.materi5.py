# ==========================================================
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# ==========================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):  # fungsi backtracking dengan batas jumlah angka 1
    # Pruning: jika jumlah_1 sudah melewati batas, berhenti
    if jumlah_1 > batas:  # jika jumlah angka 1 lebih dari batas
        return  # hentikan eksplorasi cabang ini

    # Base case
    if len(hasil) == n:  # jika panjang kombinasi sudah n
        print(hasil)  # tampilkan hasil
        return  # hentikan cabang ini

    # Pilih '0'
    biner_batas(n, batas, hasil + "0", jumlah_1)  # tambah 0 tanpa menambah jumlah_1

    # Pilih '1'
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)  # tambah 1 dan jumlah_1 bertambah 1

biner_batas(4, 2)  # kombinasi 4 digit dengan maksimal dua angka 1