num = [1,43,98,12,13,54,6,8,7,10,20,20,52,79,73]

#carilah bilangan ganjil,genap,prima

for prima in num:
    for i in range(1,prima):
        if prima % 2 == 0:
            break
    else:
        print(f"ini adalah prima :{prima}")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for ganjil in num:
    for j in range(1,ganjil):
        if ganjil % 3 == 0:
            break
        
    else:
        print(f"ini adalah ganjil :{ganjil}")
        
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for genap in num:
    for l in range(1,genap):
        if genap % 2 == 1:
            break
    else:
        print(f"ini adalah genap :{genap}")
        
        
        
