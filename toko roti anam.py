# Data roti
menu_roti = {
    "Roti Coklat": 5000,
    "Roti Keju": 6000,
    "Roti Pisang": 5500,
    "Roti Sosis": 7000,
    "Roti Tawar": 4500
}

# Fungsi tampilkan menu
def tampilkan_menu():
    print("\n=== MENU Roti Toko Bahagia ===")
    for i, (nama, harga) in enumerate(menu_roti.items(), start=1):
        print(f"{i}. {nama} - Rp{harga:,}")

# Fungsi ambil pesanan
def ambil_pesanan():
    pesanan = {}
    while True:
        tampilkan_menu()
        pilihan = input("Pilih roti (nama/ketik 'selesai' untuk selesai): ").title()
        if pilihan.lower() == "selesai":
            break
        if pilihan in menu_roti:
            jumlah = int(input(f"Jumlah {pilihan}: "))
            if pilihan in pesanan:
                pesanan[pilihan] += jumlah
            else:
                pesanan[pilihan] = jumlah
        else:
            print("Roti tidak tersedia.")
    return pesanan

# Hitung total belanja
def hitung_total(pesanan):
    total = 0
    for nama, jumlah in pesanan.items():
        total += menu_roti[nama] * jumlah
    return total

# Cetak struk
def cetak_struk(pesanan):
    print("\n=== STRUK PEMBELIAN ===")
    for nama, jumlah in pesanan.items():
        harga = menu_roti[nama]
        print(f"{nama} x{jumlah} = Rp{harga * jumlah:,}")
    total = hitung_total(pesanan)
    print(f"TOTAL = Rp{total:,}")
    print("========================")

# Jalankan program
def main():
    print("Selamat datang di Toko Roti Bahagia!")
    pesanan = ambil_pesanan()
    if pesanan:
        cetak_struk(pesanan)
    else:
        print("Tidak ada pesanan.")

if __name__ == "__main__":
    main()
