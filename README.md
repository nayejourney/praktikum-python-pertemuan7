# Praktikum Python Pertemuan 7

Repository ini berisi kumpulan latihan praktikum Python Pertemuan 7 yang membahas pengolahan file, exception handling, logging, unit testing, clean code, dan penggunaan pre-commit.

## 📁 Struktur Folder

```text
praktikum_python_pertemuan7/
│
├── latihan1_csv/
│   ├── main.py
│   └── mahasiswa.csv
│
├── latihan2_custom_exception/
│   └── main.py
│
├── latihan3_logging/
│   └── main.py
│
├── latihan4_unit_testing/
│   ├── main.py
│   └── test_main.py
│
├── latihan5_clean_code/
│   └── main.py
│
├── latihan6_pre_commit/
│   ├── main.py
│   └── .pre-commit-config.yaml
│
├── .gitignore
└── README.md
```

## 📚 Daftar Latihan

### 1. CSV File Handling
Mempelajari cara membaca dan mengolah data dari file CSV menggunakan modul `csv`, termasuk penanganan kesalahan menggunakan `try-except-finally`.

### 2. Custom Exception
Membuat exception sendiri untuk menangani kondisi kesalahan tertentu dalam program, seperti buku tidak ditemukan dan buku tidak tersedia.

### 3. Logging
Mengimplementasikan sistem logging menggunakan modul `logging` dan `RotatingFileHandler` untuk mencatat aktivitas serta kesalahan program.

### 4. Unit Testing
Menguji fungsi Python menggunakan modul `unittest` untuk memastikan program berjalan sesuai dengan hasil yang diharapkan.

### 5. Clean Code
Menerapkan prinsip clean code dengan memperbaiki code smells, seperti magic number, duplikasi kode, fungsi terlalu panjang, dan nested condition.

### 6. Pre-commit
Menggunakan pre-commit untuk menjalankan pemeriksaan kualitas kode secara otomatis dengan tools:
- Black
- Flake8
- isort

## ⚙️ Persyaratan

- Python 3.x
- Visual Studio Code (opsional)
- Git
- pip

## 🚀 Cara Menjalankan Program

1. Clone repository:

```bash
git clone https://github.com/USERNAME/praktikum-python-pertemuan7.git
```

2. Masuk ke folder proyek:

```bash
cd praktikum-python-pertemuan7
```

3. Jalankan latihan sesuai foldernya. Contoh:

```bash
python latihan1_csv/main.py
```

Ganti lokasi file sesuai latihan yang ingin dijalankan.

## 🧪 Menjalankan Unit Testing

Jalankan perintah berikut dari folder utama:

```bash
python -m unittest discover -s latihan4_unit_testing -v
```

## 🛠️ Menjalankan Pre-commit

Instalasi tools:

```bash
python -m pip install pre-commit black flake8 isort
```

Jalankan pemeriksaan:

```bash
python -m pre_commit run --all-files --config latihan6_pre_commit/.pre-commit-config.yaml
```

## 🎯 Tujuan Praktikum

Praktikum ini bertujuan meningkatkan pemahaman dan kemampuan dalam menerapkan konsep Python, mulai dari pengolahan data, penanganan kesalahan, pengujian program, hingga menjaga kualitas dan konsistensi kode.

---

**Praktikum Python Pertemuan 7**  
Dibuat sebagai dokumentasi tugas praktikum pemrograman Python.