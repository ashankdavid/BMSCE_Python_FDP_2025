class Mom:
    def cook(self):
        print("Cooking....")

class Dad:
    def sleep(self):
        print("Sleeping....")

class Child(Mom, Dad):
    def study(self):
        print("Studying...")

d = Dad() # Dad Object
m = Mom() # Mom Object
c = Child() # Child Object

d.sleep()

m.cook()

c.study()
c.cook()
c.sleep()