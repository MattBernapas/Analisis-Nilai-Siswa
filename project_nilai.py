import pandas as pd

#....data sederhana....

data = {
    "nama" : ["budi", "rahmat", "ilham", "dina", "eka"],
    "nilai" : [75, 90, 86, 80, 65],
    "kelas" : ["10A", "10A", "10B", "10B", "10B"]
}

#....ubah data ke dataframe....
df = pd.DataFrame(data)

#....menampilkan data....
print("tabel nilai siswa:\n", df)

#....hitung rata-rata nilai....
rata_rata = df["nilai"].mean()
print("\nrata-rata nilai:", rata_rata)

#.... cari siswa di atas rata-rata....
atas = df[df["nilai"] > rata_rata]
print("\nsiswa dengan nilai di atas rata-rata:\n", atas)

#.... cari siswa di bawah rata-rata....
bawah = df[df["nilai"] < rata_rata]
print("\nsiswa dengan nilai di bawah rata-rata:\n", bawah)

#.... cari siswa dengan nilai tertinggi....
nilai_max = df["nilai"].max() #cari angka nilai terbesar
tertinggi = df[df["nilai"] == nilai_max] #filter siswa yang nilainya = terbesar
print("\nsiswa dengan nilai tertinggi:\n", tertinggi)

#....simpan tabel ke file excel....
df.to_excel("nilai_siswa.xlsx", index=False)
print("\ndata berhasil di simpan ke 'nilai_siswa.xlsx'")