# Mini Project 1: Sistem Peminjaman Online
Mini Project Python dari Mata Kuliah Dasar-Dasar Pemrograman (DDP)

NAMA: Zefri Al Rizqullah
<br>
NIM: 2509116084
<br>
SISTEM INFORMASI KELAS C 2025
<br>
<br>
<h2> Flowchart minpro-pinjol:</h2>
<img width="1438" height="2216" alt="Flowchart Pinjol (Minpro part 2) drawio" src="https://github.com/user-attachments/assets/fddba3b7-3f47-413a-8947-bd484360c6a0" />

<br>
<br>
<br>

<h2>Output Menu</h2>
<img width="1538" height="309" alt="image" src="https://github.com/user-attachments/assets/50ad3581-ebec-42da-8506-31f52ba2e868" />
<p>Program pinjol ini jika dijalankan maka yang pertama akan keluar adalah Menu yang terdiri dari 5 pilihan.
Pilihan tersebut ada:
</p>
<p>1. Lihat Daftar Orang yang Pinjol, berisi data data daftar orang yang melakukan peminjaman online.</p>
<p>2. Create Peminjaman, merupakan halaman untuk mengcreate data baru orang yang melakukan peminjaman online.</p>
<p>3. Update Status Peminjaman, seharusnya ini halaman untuk mengupdate status peminjaman online dari menunggu menjadi: "disetujui"/"ditolak"/"lunas", namun saya belum mampu untuk menyelesaikan yang update ini.</p>
<p>4. Delete Pinjaman, untuk menghapus data pinjaman sesuai no hp yang diinputkan.</p>
<p>5. Exit, merupakan akhir dari program jika memilih pilihan ini.</p>
<p>Lalu diberikan sebuah inputan untuk memilih pilihan mana yang diinginkan dari 1-5, jika menginputkan selain 1-5, maka akan mengeluarkan output: "Inputan yang Anda masukan tidak valid ❌, coba lagi ya🙏"</p>
<img width="1528" height="501" alt="image" src="https://github.com/user-attachments/assets/73b71f5e-f8e9-4a1d-adf2-9ee0c99ba64d" />

<br>
<br>
<br>

<h2>Pilihan Pertama</h2>
<p>Jika masuk ke pilihan pertama, maka akan menampilkan sebuah data data peminjol yang sudah dicreate, yang berisikan no hp, nama, jumlah pinjaman, tenor, bunga, totalnya, dan status.
Namun jika data ada tercreate atau data nya kosong maka akan menampilkan output dengan pesan "Belum ada orang yang pinjol"</p>
<img width="774" height="366" alt="image" src="https://github.com/user-attachments/assets/28c47629-a49a-488c-b712-961447a48cd7" />
<img width="1219" height="364" alt="image" src="https://github.com/user-attachments/assets/d35853c7-cc60-49f3-bc0e-312e7bed07d5" />

<h2>Pilihan Kedua</h2>
<p>Masuk ke pilihan kedua yang merupakan untuk mengcreate data peminjol dengan menginputkan no hp, nama, jumlah pinjaman, dan tenor. Bunga ditentukan melalui tenor dan jumlah pinjaman yang dimana, jika tenor nya 1 tahun maka akan mendapat bunga 5% jadi: jumlah * 5 / 100, kalau tenor nya lebih dari 1 tahun dan kurang dari 5 tahun maka akan mendapat bunga 10% jadi: jumlah * 10 / 100, lalu jika tenor nya sama dengan atau lebih dari 5 tahun maka akan mendapatkan bunga 20% jadinya: jumlah * 20 / 100. Lalu terdapat total yang akan diproses dengan total = jumlah + bunga, total merupakan tagihan yang perlu dibayarkan oleh peminjol. Dan ada status yang jika setiap data di create maka akan memiliki status = menunggu.</p>
<img width="1600" height="652" alt="image" src="https://github.com/user-attachments/assets/8dc3563d-dfdf-444e-b041-ab6257f83bde" />

<br>
<br>
<br>

<h2>Pilihan Ketiga</h2>
Masih belum saya kerjakan, jadi hanya menampilkan pesan "Coming Soon".
<img width="1589" height="256" alt="image" src="https://github.com/user-attachments/assets/2aacf35e-d611-4cea-afa5-ad77300e44d9" />

<br>
<br>
<br>

<h2>Pilihan Keempat</h2>
Pada pilihan keempat merupakan program yang menghapus data peminjol sesuai dengan no hp yang diinputkan. Akan menampilkan semua data peminjol lalu user diminta untuk menginputkan salah satu no hp yang ingin dihapus, kalau terdapat kesalahan nomor yang diinputkan atau tidak sesuai maka akan menampilkan pesan "Nomor yang Anda masukkan tidak terdaftar!". Dan jika tidak ada data peminjol maka akan menampilkan output pesan "Belum ada orang yang pinjol".
<img width="1591" height="275" alt="image" src="https://github.com/user-attachments/assets/a0716c7a-b128-4fb5-9152-13c78df60d4c" />
<img width="1569" height="318" alt="image" src="https://github.com/user-attachments/assets/df97a3f4-6dc0-41f6-8f4f-a60f89ca21f1" />

<br>
<br>
<br>

<h2>Pilihan Kelima</h2>
Merupakan akhir dari program jika menginputkan 5, pilihan ini adalah satu satu nya untuk keluar dari program tersebut.
<img width="1573" height="266" alt="image" src="https://github.com/user-attachments/assets/4e2ab321-e7a0-4cec-8c04-33193c0ea1e4" />

