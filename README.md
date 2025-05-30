# Tubes Python Game

## Deskripsi Proyek

**Tubes Python Game** adalah permainan bergenre **Tower Defense** yang dibangun menggunakan Python dan library **Pygame**. Dalam game ini, pemain bertugas untuk mempertahankan markas dari gelombang musuh dengan membangun serta meng-upgrade menara pertahanan (turret). Pemain harus menyusun strategi penempatan turret dan mengelola sumber daya (uang) secara efisien agar dapat menghadapi musuh yang semakin kuat di setiap level.

---

## Dependensi Paket (Library)

Game ini membutuhkan pustaka berikut:

- `pygame`: Untuk menangani grafis dan gameplay.
- `json`: Untuk membaca data level dari file `.tmj`.

Untuk menginstal `pygame`, jalankan perintah berikut:

```bash
pip install pygame
```

---

## Cara Menjalankan Aplikasi

1. Pastikan semua dependensi telah diinstal.
2. Jalankan file utama menggunakan Python:

```bash
python main.py
```

---

## Cara Bermain

### Tujuan:
Pertahankan markas Anda dari musuh yang berjalan dari sisi kiri ke kanan layar. Jika musuh mencapai ujung jalur, Anda kehilangan 1 poin kesehatan. Permainan berakhir jika poin kesehatan Anda habis.

### Membangun Turret:
- Klik tombol **"BUY TURRET"** pada panel kanan untuk mengaktifkan mode penempatan.
- Kursor akan berubah menjadi gambar turret.
- Klik pada area kosong di peta untuk menempatkan turret.
- Pastikan Anda memiliki cukup uang.

### Upgrade Turret:
- Klik pada turret yang sudah ditempatkan untuk memilihnya.
- Klik tombol **"UPGRADE TURRET"** di panel untuk meningkatkan turret.
- Upgrade meningkatkan jangkauan, cooldown, dan damage turret.

### Memulai Gelombang Musuh:
- Klik tombol **"BEGIN"** untuk memulai serangan musuh.
- Turret akan otomatis menembak musuh dalam jangkauannya.

### Kecepatan Permainan:
- Klik tombol **"FAST FORWARD"** untuk mempercepat jalannya game.

### Kesehatan & Uang:
- Kesehatan ditunjukkan dengan ikon hati.
- Uang ditunjukkan dengan ikon koin.
- Anda mendapatkan uang dari setiap musuh yang dikalahkan dan hadiah di akhir level.

### Game Over:
- Permainan berakhir jika kesehatan mencapai 0.
- Jika semua level berhasil dilewati, Anda menang.

### Restart:
- Setelah game over, akan muncul tombol **"RESTART"** untuk memulai ulang game dari awal.

---

## UML Class Diagram

Diagram berikut menggambarkan struktur kelas dari aplikasi ini:

![UML Diagram](./UML%20diagram.jpg)

---

## Kontributor

- [George Haansraj](https://github.com/GeorgeHaansraj)
- [Muhammad Arkan S](https://github.com/7-166-MuhammadArkanS)
- [Zenn](https://github.com/xzyzenn)
- [Bonifasius Ezra Mariano](https://github.com/14-123140196-BonifasiusEzraMariano)

---

## Referensi Aset

- **Enemy Sprite**:  
  [Free Zombie Villager Chibi Character](https://craftpix.net/freebies/free-zombie-villager-chibi-character-sprites/?num=1&count=51&sq=zombie&pos=9)
- **Map Game**:  
  [Free Forest Battle Backgrounds](https://craftpix.net/freebies/free-forest-battle-backgrounds/?num=1&count=124&sq=forest&pos=3)
- **Tower Cursor**:  
  [Free Game Icons of Fantasy Things Pack 15](https://craftpix.net/freebies/free-game-icons-of-fantasy-things-pack-15/?num=1&count=57&sq=hammer&pos=8)
- **Tower Assets**:  
  [Free Stone Tower Game Assets](https://craftpix.net/freebies/free-stone-tower-game-assets/?num=1&count=166&sq=tower&pos=5)

---

## Repository

🔗 [https://github.com/GeorgeHaansraj/tubes-python-game](https://github.com/GeorgeHaansraj/tubes-python-game)