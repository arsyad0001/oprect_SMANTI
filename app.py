import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

# 1. Load variabel rahasia dari file .env
load_dotenv()

app = Flask(__name__)
# Mengambil secret key Flask dari file .env
app.secret_key = os.getenv("FLASK_SECRET_KEY", "default_secret_key")

# Deteksi folder tempat app.py berada secara otomatis
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_PATH = os.path.join(BASE_DIR, 'credentials.json')

# 2. Fungsi untuk melakukan koneksi ke Google Sheets API
def get_google_sheet():
    # Mengatur hak akses (scope) ke Google Drive & Sheets
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    
    # Autentikasi menggunakan file credentials.json dengan jalur absolut
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_PATH, scope)
    client = gspread.authorize(creds)
    
    # Buka spreadsheet berdasarkan SPREADSHEET_ID yang ada di file .env
    spreadsheet = client.open_by_key(os.getenv("SPREADSHEET_ID"))
    return spreadsheet.sheet1


# 3. Route Utama: Menampilkan Halaman Web Form
@app.route('/')
def index():
    return render_template('index.html')


# 4. Route Submit: Menerima Data dari Form & Simpan ke Google Sheets
@app.route('/submit', methods=['POST'])
def submit():
    # Ambil data dari input form HTML berdasarkan attribute 'name'
    nama = request.form.get('nama')
    kelas = request.form.get('kelas')
    panitia = request.form.get('panitia')
    
    # Ambil waktu pendaftaran otomatis
    waktu_daftar = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Panggil fungsi koneksi Google Sheet
        sheet = get_google_sheet()
        
        # Masukkan data sebagai baris baru di Google Sheet
        sheet.append_row([waktu_daftar, nama, kelas, panitia])
        
        # Kirim notifikasi sukses ke tampilan HTML
        flash('Pendaftaran berhasil dikirim! Data kamu sudah tersimpan.', 'success')
    except Exception as e:
        print(f"Error Google Sheets: {e}")
        # Kirim notifikasi error jika gagal
        flash('Terjadi kesalahan saat menyimpan data. Cek file .env atau credentials.json.', 'error')

    return redirect('/')


# 5. Jalankan Web Server Flask
if __name__ == '__main__':
    app.run(debug=True)