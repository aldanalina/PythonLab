n = int(input("san engiz: "))
for i in range(1,10,1):
    for j in range(1,n+1,1):
        print(f"{i} * {j} = {i*j}", end='\t')
    print()