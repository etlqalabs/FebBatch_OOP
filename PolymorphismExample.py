# Method overloading ( not possible in python )
'''
class Math:
    def add(self,n1,n2):
        return n1+n2

    def add(self,n1,n2,n3):
        return n1+n2+n3

math =  Math()
print(math.add(2,4,6))
'''

# Methoding overiding
class Bird:
    def fly(self):
        print("Bird can fly")

class Penguine1(Bird):
    def fly(self):
        print("Penguine can't fly")

class Penguine2(Bird):
    pass


pengu1 = Penguine1()
pengu1.fly()

pengu2 = Penguine2()
pengu2.fly()

pengu3 = Bird()
pengu3.fly()

