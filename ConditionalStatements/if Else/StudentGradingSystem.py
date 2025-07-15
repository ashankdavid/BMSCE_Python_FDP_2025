m1 = int(input("Enter the Marks1: "))
m2 = int(input("Enter the Marks2: "))
m3 = int(input("Enter the Marks3: "))
m4 = int(input("Enter the Marks4: "))
m5 = int(input("Enter the Marks5: "))
total_marks = 500

percentage = ((m1+m2+m3+m4+m5)/total_marks) * 100

if percentage >= 75:
    print("A")
elif percentage >= 50:
    print("B")
elif percentage >=30:
    print("C")
else:
    print("Fail")