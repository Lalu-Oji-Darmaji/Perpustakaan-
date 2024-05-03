class Buku:
    def __init__(self, judul, penulis, genre, status):
        self.judul = judul
        self.penulis = penulis
        self.genre = genre
        self.status = status

    def __str__(self):
        return f"{self.judul} - {self.penulis} ({self.genre}) - status: {self.status}"

class Perpustakaan:
    def __init__(self):
        self.koleksi_buku = []

    def tampilkan_buku(self):
        if self.koleksi_buku:
            print("-- Daftar Buku --")
            for buku in self.koleksi_buku:
                print(buku)
        else:
            print("Koleksi buku masih kosong.")

    def cari_buku(self, judul):
        found = False
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                print(buku)
                found = True
                break
        if not found:
            print(f"Buku dengan judul '{judul}' tidak ditemukan.")

    def pinjam_buku(self, judul, anggota):
        found = False
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                found = True
                if buku.status == "Tersedia":
                    buku.status = "Dipinjam"
                    anggota.buku_pinjaman.append(buku)
                    print(f"Buku '{buku.judul}' berhasil dipinjam oleh {anggota.nama}.")
                else:
                    print(f"Buku '{buku.judul}' tidak tersedia untuk dipinjam.")
                break
        if not found:
            print(f"Buku dengan judul '{judul}' tidak tersedia di perpustakaan.")

    def kembalikan_buku(self, judul, anggota):
        found = False
        for buku in anggota.buku_pinjaman:
            if buku.judul.lower() == judul.lower():
                found = True
                buku.status = "Tersedia"
                anggota.buku_pinjaman.remove(buku)
                print(f"Buku '{buku.judul}' berhasil dikembalikan oleh {anggota.nama}.")
                break
        if not found:
            print(f"Anda tidak memiliki buku dengan judul '{judul}' untuk dikembalikan.")

class Anggota:
    def __init__(self, nama, ID):
        self.nama = nama
        self.ID = ID
        self.buku_pinjaman = []

    def tampilkan_buku_pinjaman(self):
        if self.buku_pinjaman:
            print(f"-- Buku Pinjaman {self.nama} --")
            for buku in self.buku_pinjaman:
                print(buku)
        else:
            print(f"{self.nama} tidak memiliki buku pinjaman.")

   
    def main():
        buku1 = Buku("Bumi", "Tere Liye", "Fiksi", "Tersedia")
        buku2 = Buku("Laskar Pelangi", "Andrea Hirata", "Fiksi", "Tersedia")
        buku3 = Buku("Filosofi Terbang", "Dewi Lestari", "Fiksi", "Dipinjam")

        perpustakaan = Perpustakaan()
        perpustakaan.koleksi_buku.extend([buku1, buku2, buku3])

        anggota1 = Anggota("Andi", 12345)
        anggota2 = Anggota("Budi", 56789)

        print("\n-- Menu Perpustakaan --")
        print("1. Tampilkan Daftar Buku")
        print("2. Cari Buku")
        print("3. Pinjam Buku")
        print("4. Kembalikan Buku")
        angka = int(input("Pilih Menu : "))

        if angka == 1:
            perpustakaan.tampilkan_buku()
        elif angka == 2:
            judul = input("Input judul buku: ")
            perpustakaan.cari_buku(judul)
        elif angka == 3:
            judul = input("Buku yang ingin dipinjam: ")
            perpustakaan.pinjam_buku(judul, anggota1)  
        elif angka == 4:
            judul = input("Buku yang ingin dikembalikan: ")
            perpustakaan.kembalikan_buku(judul, anggota2)  
        else:
            print("Anda salah memilih menu.")

if __name__ == "__main__":
    Anggota.main()
