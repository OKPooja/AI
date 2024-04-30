import math
import random
from math import sin

def f1(x):
    return sin(x)
    
def f2(x):
    return -x**2

def f3(x):
    return -5*x**2 + 3*x + 6

def best_neighbour(f,x,step = 0.1):
    if(f(x - step) > f(x)):
        return x - step
    if(f(x + step) > f(x)):
        return x + step
    else:
        return x
        
def hill_climbing(f, x, max_iterations = 1000):
    for i in range(max_iterations):
        neighbour = best_neighbour(f, x)
        if(f(neighbour) > f(x)):
            x = neighbour
        else:
            break
    return x
        
if __name__ == "__main__":
    ranges = [(-math.pi, math.pi), (-1,1), (-100,100)]
    functions = [f1, f2, f3]
    
    for i, f in enumerate(functions):
        x = random.uniform(ranges[i][0], ranges[i][1])
        best_pos = round(hill_climbing(f, x),4)
        value = round(f(best_pos),4)
        print(f'For function {i + 1}, the best position is {best_pos} with a value of {value}.')
