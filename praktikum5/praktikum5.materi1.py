# ==========================================================
# Contoh Rekursi 1: Faktorial
# ==========================================================

def faktorial(n):  # fungsi rekursif untuk menghitung faktorial
    # Base case: berhenti ketika n = 0
    if n == 0:  # jika n sama dengan 0
        return 1  # kembalikan 1 karena 0! = 1

    # Recursive case: masalah diperkecil menjadi faktorial(n-1)
    return n * faktorial(n - 1)  # n dikali hasil faktorial dari (n-1)

print(faktorial(5)) # memanggil fungsi faktorial dengan input 5, Output: 120
print(faktorial(int(input("masukan angka yang ingin di faktorialkan: "))))  # atau input manual angkanya