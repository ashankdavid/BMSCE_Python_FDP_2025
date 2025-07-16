class India:
    def capital(self):
        print("New Delhi")


class USA:
    def capital(self):
        print("Washington DC")


objIND = India()
objUSA = USA()

objIND.capital()  # Same Function printing NewDelhi here
objUSA.capital()  # Same Function printing Washington DC here

# here in the above program i can say that capital function has become polymorphic in nature...