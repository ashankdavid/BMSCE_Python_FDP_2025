n = int(input("Enter a Num: "))
is_Prime = True
if n<2:
    is_Prime = False
else:
    for i in range(2, n):
        if n%i==0:
            is_Prime = False
            break

print("Prime" if is_Prime else "Not Prime")