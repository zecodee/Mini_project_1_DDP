# © 2025 Zefri Al Rizqullah | 2509116084.

pinjol = []

while True:
    print("================ Sistem Pinjaman Online MoyaMoya ================")
    print("1. Lihat Daftar Orang yang Pinjol")
    print("2. Create Pinjaman")
    print("3. Update Status Pinjaman")
    print("4. Delete Pinjaman")
    print("5. Exit")
    pilih_menu = int(input("\nPilih menu berikut (1-5): "))
    print("============ This Systems Made by Zefri Al Rizqullah ============")
    
    if pilih_menu == 1:
        print("\n")
        print("=" * 19, "Daftar Orang yang Pinjol!", "=" * 19)
        
        if pinjol == []:
            print("Belum ada orang yang pinjol")
            
        else:
            no = 1
            for (no_hp, nama, jumlah, tenor, bunga, total, status) in pinjol:
                print(f"{no}. {no_hp} | {nama} | Pinjam: Rp. {jumlah:,} | Tenor: {tenor} tahun | Bunga: Rp. {bunga:,} | Total: Rp. {total:,} | Status: {status}")
                no += 1
        
        print("=" * 65)
        print("\n")
        
    elif pilih_menu == 2:
        print("\n")
        print("=" * 17, "Tambahkan Orang yang Pinjol!", "=" * 17)

        no_hp = int(input("Masukan nomor peminjol: "))
        nama = input("Masukan nama peminjol: ")
        jumlah = int(input("Masukan jumlah yang dipinjol: "))
        tenor = int(input("Masukan tenor nya (tahun): "))
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
            
        total = jumlah + bunga
        status = "menunggu"
        
        pinjol.append((no_hp, nama, jumlah, tenor, bunga, total, status))
        print("Pinjaman berhasil didaftarkan!")
        
        print("=" * 65)
        print("\n")
        
    elif pilih_menu == 3:
        print("\n")
        print("=" * 16, "Update Status Orang yang Pinjol", "=" * 16)

        print("Cooming Soon")
        
        print("=" * 65)
        print("\n")


    elif pilih_menu == 4:
        print("\n")
        print("=" * 17, "Hapus Data orang yang Pinjol!", "=" * 17)
        
        if pinjol == []:
            print("Belum ada orang yang pinjol")
        
        else:
            no = 1
            for (no_hp, nama, jumlah, tenor, bunga, total, status) in pinjol:
                print(f"{no}. {no_hp} | {nama} | Pinjam: Rp. {jumlah:,} | Tenor: {tenor} tahun | Bunga: Rp. {bunga:,} | Total: Rp. {total:,} | Status: {status}")
                no += 1
                
            hapus = int(input("Masukan nomor hp yang mau dihapus: "))
            for data in pinjol:
                if data[0] == hapus:
                    pinjol.remove(data)
                    print("Data berhasil dihapus")
                    break
                
                else:
                    print("Nomor yang Anda masukkan tidak terdaftar!")
                    break
            
        print("=" * 65)
        print("\n")

    elif pilih_menu == 5:
        print("\nAnda keluar dari sistem kami 😓")
        break
    
    else:
        print("\nInputan yang Anda masukan tidak valid ❌, coba lagi ya🙏\n")