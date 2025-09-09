# 📊 Analisis Nilai Siswa

Project ini dibuat untuk **menganalisis data nilai siswa** menggunakan Python.  
Output project berupa **file Excel** yang berisi data lengkap, analisis ringkasan, dan grafik otomatis.  
Cocok untuk latihan **Python Data Analysis** bagi pemula.

---

## ✨ Fitur Utama
- 📋 **Input Data Siswa** → Nama, Kelas, dan Nilai
- 🔍 **Analisis Otomatis**:
  - Rata-rata nilai
  - Nilai tertinggi
  - Nilai terendah
- 📑 **Ekspor ke Excel** dengan 3 sheet:
  1. **Data Siswa** → berisi daftar nilai siswa
  2. **Analisis** → ringkasan nilai rata-rata, tertinggi, terendah
  3. **Grafik** → diagram batang perbandingan nilai siswa

---

## 🛠️ Teknologi yang Digunakan
- [Python 3](https://www.python.org/)  
- [pandas](https://pandas.pydata.org/) → untuk mengolah data  
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/) → untuk ekspor Excel & grafik  

---

## 📂 Struktur Project

AI_Project/ │ ├── analisis.py              # kode Python utama ├── requirements.txt         # daftar library yang dibutuhkan ├── README.md                # dokumentasi project └── hasil_analisis_keren.xlsx (opsional, file output)

---

## 🚀 Instalasi
1. Clone repository:
   ```bash
   git clone https://github.com/USERNAME/Analisis-Nilai-Siswa.git
   cd Analisis-Nilai-Siswa

2. Install dependencies:

pip install -r requirements.txt




---

▶️ Cara Menjalankan

Jalankan perintah berikut di terminal:

python analisis.py

Hasil akan tersimpan di file:

hasil_analisis_keren.xlsx

Buka file tersebut di Microsoft Excel atau LibreOffice Calc.
Di dalamnya terdapat:

Sheet 1: Data Siswa

Sheet 2: Analisis Ringkasan

Sheet 3: Grafik (diagram batang nilai siswa)



---

📸 Contoh Output

Data Siswa

Nama	Kelas	Nilai

Budi	X	80
Ani	X	90
Siti	XI	75
Rian	XI	85


Analisis

Kategori	Nilai

Rata-rata	82.5
Nilai Tertinggi	90
Nilai Terendah	75


Grafik
(Diagram batang perbandingan nilai siswa akan muncul di Excel)
