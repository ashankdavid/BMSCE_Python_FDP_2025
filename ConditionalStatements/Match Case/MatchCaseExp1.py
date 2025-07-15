fruit = input("Enter a Fruit: ")

match fruit:
    case "Apple":
        print("You have given an Apple!")
    case "Mango":
        print("You have given an Mango!")
    case "Orange":
        print("You have given an Orange!")
    case _:
        print("Maybe some random fruit or invalid entry!")