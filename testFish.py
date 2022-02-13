class Shark() :
    def swim(self):
        print("The shark is swimming")
    
    def swim_backward(self):
        print("Sharks cannot swim backward but can sink backward")
    
    def skeleton(self):
        print("The shark's skeleton is made of cartilage")

class Clownfish():
    def swim(self):
        print("Clownfish is swimming")
    
    def swim_backward(self):
        print("the clownfish can swim backward")

    def skeleton(self):
        print("the clownfish's skeleton is made of bone")

def in_the_pacific(fish):
    fish.swim()

shark1 = Shark()
shark1.skeleton()

clownsfish1 = Clownfish()
clownsfish1.skeleton()

print("\n")

for fish in (shark1,clownsfish1):
    fish.swim()
    fish.swim_backward()
    fish.skeleton()

in_the_pacific(shark1)
in_the_pacific(clownsfish1)
