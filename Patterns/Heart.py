rows = 6
cols = 7

for i in range(rows):
    for j in range(cols):
        if i==0 and j%3!=0:
            print(" * ", end='')
        elif i==1 and j%3==0:
            print(" * ", end='')
        elif i-j==2:
            print(" * ", end='')
        elif i+j==8:
            print(" * ", end='')
        else:
            print("   ", end='')
    print()