n = int(input("Enter a Num: "))
fact = 1
for i in range(1, n+1):
    fact *= i

print(f"Factorial is: {fact}")