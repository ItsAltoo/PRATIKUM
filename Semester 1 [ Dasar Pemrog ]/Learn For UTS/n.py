# List bilangan
nim = [2,4,1,1,1,0,2,4,4,1,2,5,0]

# Inisialisasi list untuk hasil
ganjil = []
genap = []
prima = []

# Proses pencarian
for n in nim:
    # Memeriksa bilangan ganjil atau genap
    if n % 2 == 0:
        genap.append(n)
    else:
        ganjil.append(n)

    # Memeriksa bilangan prima
    if n > 1:
        is_prime = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            prima.append(n)
            

# Menampilkan hasil
print("Bilangan ganjil:", ganjil)
print("Bilangan genap:", genap)
print("Bilangan prima:", prima)
