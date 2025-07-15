n = int(input("Enter a Num: "))
is_Prime = True
if n<2:
    is_Prime = False
else:
    i=2
    while i<n:
        if n%i==0:
            is_Prime = False
            break
        i+=1

print("Prime" if is_Prime else "Not Prime")