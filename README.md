# 📋 Portal Pendaftaran Panitia Acara Sekolah

Web aplikasi pendaftaran panitia acara sekolah interaktif berbasis **Python (Flask)** yang terintegrasi secara otomatis dengan **Google Sheets API** sebagai basis penyimpanan data pendaftar.

---

## 🛠️ Tech Stack
- **Frontend:** HTML5, CSS3 (Responsive Design)
- **Backend:** Python (Flask Framework)
- **Database / API Integration:** Google Sheets API (`gspread`, `oauth2client`)
- **Environment Management:** `python-dotenv`

---

## 🚀 Fitur Utama
1. **Informasi Divisi:** Penjelasan tugas untuk Panitia Perlengkapan dan Panitia Keamanan.
2. **Formulir Pendaftaran:** Input data pendaftar (Nama Lengkap, Kelas, Pilihan Divisi).
3. **Real-time Google Sheets Storage:** Data dari formulir otomatis tersimpan ke Google Sheets tanpa penyimpanan lokal.
4. **Environment Security:** Seluruh kunci rahasia API disimpan aman menggunakan file `.env` dan diabaikan dari repositori melalui `.gitignore`.

---

## ⚙️ Cara Menjalankan Aplikasi di Komputer Lokal

### 1. Clone Repositori
```bash
git clone [https://github.com/username-kamu/oprec-sekolah.git](https://github.com/username-kamu/oprec-sekolah.git)
cd oprec-sekolah