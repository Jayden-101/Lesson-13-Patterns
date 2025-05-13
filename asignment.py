r = int(input("Enter the totalNumber of rows: "))

print("Mirrored Right triangle star pattern")
for i in range(1,r+1):
    for j in range(1,r+1):
        if(j <= r -i):
            print('', end = '')
        else:
            print('*', end = '')
    print()