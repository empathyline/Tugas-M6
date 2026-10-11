data_pelanggan = ("Andi", "Premium")
berat_kardus = [40, 35, 30]
nama, status_member = data_pelanggan
total_berat = sum(berat_kardus)
vip = status_member == "Premium" or total_berat > 100

print(f"Nama pelanggan: {nama}")
print(f"Total berat: {total_berat} kg")
print(f"Apakah pengiriman VIP? {vip}")