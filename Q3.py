ipk = float(input("Masukkan IPK: "))
riwayat_nilai = ["A", "B", "A", "C", "B"]
hasil = ipk >= 3.50 and "E" not in riwayat_nilai

print(f"Apakah mahasiswa lolos seleksi? {hasil}")