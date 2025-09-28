# © 2025 Zefri Al Rizqullah | 2509116084.
# from prettytable import PrettyTable
from pwinput import pwinput

pinjol = []
users = {
    "admin": {"password": "123", "role": "admin"},
    "olaa": {"password": "123", "role": "user"},
    "zefry": {"password": "123", "role": "user"},
}

def read():
    no = 1
    for (no_hp, nama, jumlah, tenor, bunga, total, status, role) in pinjol:
        print(f"{no}. {no_hp} | {nama} | Pinjam: Rp. {jumlah:,} | Tenor: {tenor} tahun | Bunga: Rp. {bunga:,} | Total: Rp. {total:,} | Status: {status}")
        no += 1
        
def read_user(username):
    no = 1
    for (no_hp, nama, jumlah, tenor, bunga, total, status, role) in pinjol:
        if role == username:
            print(
                f"{no}. {no_hp} | {nama} | Pinjam: Rp. {jumlah:,} | Tenor: {tenor} tahun | Bunga: Rp. {bunga:,} | Total: Rp. {total:,} | Status: {status}"
                )
            no += 1
        
def create(role):
    try:
        no_hp = int(input("Masukan nomor peminjol: "))
        nama = input("Masukan nama peminjol: ")
        jumlah = int(input("Masukan jumlah yang dipinjol: "))
        tenor = int(input("Masukan tenor nya (tahun): "))
    
    except ValueError:
        print("Inputan yang Anda masukkan tidak valid")
    
    if tenor == 1:
        bunga = jumlah * 5 / 100
        print("Mendapat bunga 5%")
    elif tenor > 1 and tenor < 5:
        bunga = jumlah * 10 / 100
        print("Mendapat bunga 10%") 
    elif tenor >= 5:
        bunga = jumlah * 20 / 100
        print("Mendapat bunga 20%")
    else:
        print("Inputan yang anda masukan tidak sesuai")
        return
        
    total = jumlah + bunga
    status = "menunggu"
    
    pinjol.append([no_hp, nama, jumlah, tenor, bunga, total, status, role])
    print("Pinjaman berhasil didaftarkan!")

def update():
    try:
        update = int(input("Masukan nomor hp yang mau diedit: "))
    except ValueError:
        print("Input harus berupa angka!")
        return
    
    for data in pinjol:
        if data[0] == update:
            new_status = input("Masukan status terbaru ('ditolak'/'diterima'/'lunas'/'telat'): ")
            
            if new_status in ["ditolak", "diterima", "lunas", "telat"]:
                data[6] = new_status
                print(f"Status berhasil diubah menjadi {new_status}")
            elif new_status == "":
                print("Status tidak ada yang berubah")
            else:
                print("Status yang anda masukkan tidak valid!")
            break
        else:
            print("Nomor yang Anda masukkan tidak terdaftar!")
            break
        
def delete():
    try:
        hapus = int(input("Masukan nomor hp yang mau dihapus: "))
    except ValueError:
        print("Input harus berupa angka!")
        return
    
    for data in pinjol:
        if data[0] == hapus:
            pinjol.remove(data)
            print("Data berhasil dihapus")
            break
        
        else:
            print("Nomor yang Anda masukkan tidak terdaftar!")
            break

def login():
    print("=========== Login Sistem Pinjaman Online Mozarela ===========")
    username = input("Username: ")
    password = pwinput("Password: ", "*")

    if username in users and users[username]["password"] == password:
        role = users[username]["role"]
        print(f"\nLogin berhasil sebagai {role}")
        return username, role
    else:
        print("Login gagal, coba ulang lagi!")
        exit()

username, role = login()

while True:
    print("================ Sistem Pinjaman Online Mozarela ================")
    
    try:
        if role == "admin":
            print("1. Lihat Semua Pinjaman")
            print("2. Update Status Pinjaman")
            print("3. Delete Pinjaman")
            print("4. Logout")
            print("5. Exit")
            pilih_menu = int(input("\nPilih menu berikut (1-5): "))
        else:
            print("1. Lihat Pinjaman Anda")
            print("2. Create Pinjaman")
            print("3. Logout")
            print("4. Exit")
            pilih_menu = int(input("\nPilih menu berikut (1-4): "))
    except ValueError:
        print("Input menu harus berupa angka!")
        continue
        
    print("============ This Systems Made by Zefri Al Rizqullah ============")
    
    if role == "admin":
        if pilih_menu == 1:
            print("\n")
            print("="*22,"Daftar Semua Pinjam", "="*22)
            if pinjol == []:
                print("Belum ada orang yang pinjol")
            else:
                read()
            print("=" * 65, "\n")

        elif pilih_menu == 2:
            print("\n")
            print("="*21,"Update Status Pinjam!", "="*21 )
            if pinjol == []:
                print("Belum ada orang yang pinjol")
            else:
                read()
                update()
            print("=" * 65, "\n")

        elif pilih_menu == 3:
            print("\n")
            print("="*22,"Hapus Data Pinjaman", "="*22)
            if pinjol == []:
                print("Belum ada orang yang pinjol")
            else:
                read()
                delete()
            print("=" * 65, "\n")

        elif pilih_menu == 4:
            print("\nAnda telah logout dari sistem kami 😓")
            username, role = login()

        elif pilih_menu == 5:
            print("\nAnda keluar dari sistem kami 😓")
            break
        else:
            print("Input Anda tidak valid")

    else: 
        if pilih_menu == 1:
            print("\n")
            print("="*25, "Pinjaman Saya", "="*25)
            if pinjol == []:
                print("Belum ada orang yang pinjol")
            else:
                read_user(username)
            print("=" * 65, "\n")

        elif pilih_menu == 2:
            print("\n")
            print("="*21, "Ajukan Pinjaman Baru!", "="*21)
            create(username)
            print("=" * 65, "\n")

        elif pilih_menu == 3:
            print("\nAnda telah logout dari sistem kami 😓")
            username, role = login()

        elif pilih_menu == 4:
            print("\nAnda keluar dari sistem kami 😓")
            break
        else:
            print("Input Anda tidak valid")
