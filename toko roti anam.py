# Data produk supermarket
produk = {
    "Beras 5kg": 65000,
    "Minyak Goreng 2L": 28000,
    "Gula 1kg": 14000,
    "Telur 1kg": 23000,
    "Sabun Mandi": 5000,
    "Shampoo": 12000
}

# Fungsi tampilkan produk
def tampilkan_produk():
    print("\n=== DAFTAR PRODUK SUPERMARKET ===")
    for i, (nama, harga) in enumerate(produk.items(), 1):
        print(f"{i}. {nama} - Rp{harga:,}")

# Fungsi ambil pesanan pelanggan
def ambil_pesanan():
    pesanan = {}
    while True:
        tampilkan_produk()
        pilihan = input("Masukkan nama produk (atau ketik 'selesai' untuk checkout): ").title()
        if pilihan.lower() == 'selesai':
            break
        elif pilihan in produk:
            try:
                jumlah = int(input(f"Jumlah {pilihan}: "))
                if pilihan in pesanan:
                    pesanan[pilihan] += jumlah
                else:
                    pesanan[pilihan] = jumlah
            except ValueError:
                print("Masukkan jumlah dalam angka!")
        else:
            print("Produk tidak tersedia.")
    return pesanan

# Fungsi hitung total belanja
def hitung_total(pesanan):
    return sum(produk[nama] * jumlah for nama, jumlah in pesanan.items())

# Fungsi cetak struk
def cetak_struk(pesanan):
    print("\n========= STRUK BELANJA =========")
    for nama, jumlah in pesanan.items():
        harga = produk[nama]
        subtotal = harga * jumlah
        print(f"{nama} x{jumlah} = Rp{subtotal:,}")
    total = hitung_total(pesanan)
    print("---------------------------------")
    print(f"TOTAL BAYAR: Rp{total:,}")
    print("Terima kasih telah berbelanja!")
    print("=================================")

# Fungsi utama
def main():
    print("Selamat Datang di Supermarket Pintar!")
    pesanan = ambil_pesanan()
    if pesanan:
        cetak_struk(pesanan)
    else:
        print("Tidak ada pembelian.")

if __name__ == "__main__":
    main()
