# Declarative knowledge is a statement of facts
# Imperative knowledge is a sequence of steps or the recipe of how to do something

import os
import random
import math

print("Hello world", os.getcwd())

def find_sqrt(x, n=8):
    g = random.randint(0, x)
    for i in range(n):
        if (g * g == x):
            return g
        g = (g + ( x / g )) / 2
    return x, g, math.sqrt(x)
        
if __name__ == "__main__":
    
    #for i in range (10):
    #   print(find_sqrt(random.randint(0, 100000)))
    pass