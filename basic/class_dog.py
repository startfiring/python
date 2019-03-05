
class dog:
    tail = True

    def __init__(self, size, color, name):
        self.size = size
        self.color = color
        self.name = name
    
    def bark(self):
        print(self.name)

myDog = dog("big", "white", "dangdang")

if myDog.tail == True:
    print("my dog has a tail")

myDog.bark()