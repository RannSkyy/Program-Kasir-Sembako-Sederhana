# ================================
# PROGRAM KASIR SEDERHANA
# ================================

# Daftar barang
barang = {
    "1": {"nama": "Beras", "harga": 12000},
    "2": {"nama": "Gula", "harga": 8000},
    "3": {"nama": "Minyak", "harga": 15000},
    "4": {"nama": "Telur", "harga": 20000},
    "5": {"nama": "Susu", "harga": 10000}
}

total = 0
keranjang = []

print("=" * 35)
print("       PROGRAM KASIR")
print("=" * 35)
print("Daftar Barang:")
print("-" * 35)

for kode, item in barang.items():
    print(f"{kode}. {item['nama']} - Rp {item['harga']}")

print("-" * 35)

while True:
    kode = input("Masukkan kode barang (0 untuk selesai): ")

    if kode == "0":
        break
    elif kode in barang:
        jumlah = int(input("Jumlah beli: "))
        subtotal = barang[kode]["harga"] * jumlah
        total += subtotal

        keranjang.append({
            "nama": barang[kode]["nama"],
            "jumlah": jumlah,
            "subtotal": subtotal
        })

        print("Barang ditambahkan.\n")
    else:
        print("Kode barang tidak valid!\n")

print("\n========== STRUK BELANJA ==========")
for item in keranjang:
    print(f"{item['nama']} x{item['jumlah']} = Rp {item['subtotal']}")

print("-" * 35)
print(f"Total Bayar : Rp {total}")

uang = int(input("Uang Dibayar : Rp "))
kembalian = uang - total

print(f"Kembalian   : Rp {kembalian}")
print("=" * 35)
print("Terima kasih telah berbelanja")