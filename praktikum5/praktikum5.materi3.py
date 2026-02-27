# ==========================================================
# Contoh Rekursi 3: Menjumlahkan Elemen List
# ==========================================================

def jumlah_list(data, index=0): # fungsi rekursif untuk menjumlahkan list
    # Base case: jika index sudah mencapai panjang list
    if index == len(data):      #jika index sama dengan panjang data
        return 0                #kembalikan 0 karna tidak ada lagi elemen
    
    #Recursive case: elemen sekarang + jumlah elemen setelahnya
    return data[index] + jumlah_list(data,index+1) # elemen sekarang ditambah hasil rekursi berikutnya

print(jumlah_list([2,4,6,8])) #output nya 20
