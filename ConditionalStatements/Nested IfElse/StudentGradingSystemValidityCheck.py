m1 = int(input("Enter the Marks1: "))
m2 = int(input("Enter the Marks2: "))
m3 = int(input("Enter the Marks3: "))
m4 = int(input("Enter the Marks4: "))
m5 = int(input("Enter the Marks5: "))
total_marks = 500

if 0 <= m1 <= 100:
    if 0 <= m2 <= 100:
        if 0 <= m3 <= 100:
            if 0 <= m4 <= 100:
                if 0 <= m5 <= 100:
                    percentage = ((m1 + m2 + m3 + m4 + m5) / total_marks) * 100
                    if percentage >= 75:
                        print("A")
                    elif percentage >= 50:
                        print("B")
                    elif percentage >= 30:
                        print("C")
                    else:
                        print("Fail")
                else:
                    print("Marks5 are Invalid")
            else:
                print("Marks4 are Invalid")
        else:
            print("Marks3 are Invaild")
    else:
        print("Marks2 are Invalid")
else:
    print("Marks1 are Invalid")