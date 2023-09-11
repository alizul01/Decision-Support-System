import pandas as pd
import random

# Jumlah alternatif yang diinginkan (ganti dengan jumlah yang Anda inginkan)
n = 100

# Inisialisasi list kosong untuk menampung data
data = []

# Generate 100 data unik dengan alternatif A1, A2, ..., An
for i in range(1, n + 1):
    alt = f'A{i}'
    c1 = random.randint(1, 4)  # Fasilitas pendukung
    c2 = random.randint(5000000, 15000000)  # Harga per meter persegi
    c3 = random.randint(2005, 2015)  # Tahun konstruksi
    c4 = random.randint(1, 10)  # Jarak dari tempat kerja (dalam kilometer)
    c5 = random.randint(1, 4)  # Sistem keamanan

    # Pastikan data yang dihasilkan unik
    while (alt, c1, c2, c3, c4, c5) in data:
        alt = f'A{i}'
        c1 = random.randint(1, 4)
        c2 = random.randint(5000000, 15000000)
        c3 = random.randint(2005, 2015)
        c4 = random.randint(1, 10)
        c5 = random.randint(1, 4)

    data.append((alt, c1, c2, c3, c4, c5))

# Simpan data ke dalam DataFrame
df = pd.DataFrame(data, columns=['alt', 'c1', 'c2', 'c3', 'c4', 'c5'])

# Simpan DataFrame ke dalam file CSV
df.to_csv('data_alternatives.csv', index=False)