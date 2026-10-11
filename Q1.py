usia = int(input("Masukkan usia: "))
departemen = input("Masukkan nama departemen: ")
hasil = usia >= 19 and "Statistika" in departemen

print(f"Apakah pendaftar memenuhi syarat? {hasil}")