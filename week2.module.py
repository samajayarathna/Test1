import random

#print(random.randrange(5,10))

#Create a function titled 'dice' that simulates the rolling of two die. It should be called once, 
# and return two integer values each chosen randomly from a 1 to 6 range

def dice():
    x = random.randrange(0,6)
    y = random.randrange(0,6)
    return x, y

z = dice()
print(z)

# to install pip install camelcase

import camelcase 
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

    


