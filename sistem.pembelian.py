class Produk:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    def tampilkan_info(self):
        print(f"Nama Produk  : {self.nama}")
        print(f"Harga Produk : Rp{self.harga:,}".replace(",", "."))
        print(f"Jumlah Beli  : {self.jumlah}")

    def hitung_total(self):
        return self.harga * self.jumlah


    def hitung_diskon(self, total_seluruh_pembelian):
        if total_seluruh_pembelian > 5000:
            return total_seluruh_pembelian * 5 // 100
        else:
            return 0

def format_rupiah(nilai):
    return f"Rp{nilai:,}".replace(",", ".")

jumlah_produk = int(input("Masukkan jumlah produk yang akan dibeli: "))

daftar_produk = []
total_seluruh_pembelian = 0

for i in range(jumlah_produk):
    print(f"\nData Produk Ke-{i + 1}")

    nama = input("Masukkan nama produk: ")
    harga = int(input("Masukkan harga produk: Rp"))
    jumlah = int(input("Masukkan jumlah beli: "))

    produk = Produk(nama, harga, jumlah)
    daftar_produk.append(produk)

    total_produk = produk.hitung_total()
    total_seluruh_pembelian += total_produk

    print(f"Total pembelian {nama}: {format_rupiah(total_produk)}")

if len(daftar_produk) > 0:
    diskon = daftar_produk[0].hitung_diskon(total_seluruh_pembelian)
else:
    diskon = 0

total_bayar = total_seluruh_pembelian - diskon

print("\n=== HASIL PEMBELIAN ===")
print(f"Total Pembelian : {format_rupiah(total_seluruh_pembelian)}")
print(f"Diskon 5%       : {format_rupiah(diskon)}")
print(f"Total Bayar     : {format_rupiah(total_bayar)}")
