num = [2,4,1,1,1,0,2,4,4,1,2,5,0]

for prima in num:
    for i in range(2,prima):
        if prima % 2 == 0:
            break
    else:
        if prima >1:
            print(f"ini adalah prima :{prima}")