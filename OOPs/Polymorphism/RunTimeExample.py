class Mom:
    def cook(self):
        print("Indian")


class Daughter(Mom):
    def cook(self):
        print("Chiense")


m = Mom()
d = Daughter()

m.cook()
d.cook()
m.cook()