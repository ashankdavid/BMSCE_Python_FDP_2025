size = 5
for i in range(size):
    for spaces in range(size-i-1):
        print(" ", end='')
    for stars in range(2*i+1):
        print("*", end='')
    print()