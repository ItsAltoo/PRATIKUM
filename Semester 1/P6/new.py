belanjaan = []

while True:
    print("\n~~~~~~~~~~~~~pilih belanjaan anda~~~~~~~~~~~~~")
    print("1.Kangkung")
    print("2.Sabun")
    print("3.Baju")
    print("4.Biskuit")
    print("5.Tampilkan hasil belanjaan")
    print("6.Keluar")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    pilihan = input("pilih pilihan anda 1-5 :")
    
    if pilihan == "1":
        pilihan = "Kangkung"
        belanjaan.append(pilihan)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"pilihan {pilihan} anda telah di tambahkan")
        
    elif pilihan == "2":
        pilihan = "Sabun"
        belanjaan.append(pilihan)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"pilihan {pilihan} anda telah di tambahkan")
        
    elif pilihan == "3":
        pilihan = "Baju"
        belanjaan.append(pilihan)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"pilihan {pilihan} anda telah di tambahkan")
    
    elif pilihan == "4":
        pilihan = "Biskuit"
        belanjaan.append(pilihan)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"pilihan {pilihan} anda telah di tambahkan")
        
    elif pilihan == "5":
        print("\n ~~~berikut adalah pilihan anda~~~")
        for i, pilihan in enumerate(belanjaan, 1):
                print(f"{i}. {pilihan}")
    elif pilihan == "6":
        print("Program telah di hentikan")
        break
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("pilihan hanya 1-5")