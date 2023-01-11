from random import seed
from random import random

import prob_calculator
from prob_calculator import Hat
from prob_calculator import experiment

print()

hat1=Hat(yellow=3,blue=2,green=6,red=7)
print()
num_balls_drawn=5
print(hat1.draw(num_balls_drawn))

print()

probability=experiment(hat=hat1,expected_balls={"red":2,"green":1},num_balls_drawn=5,num_experiment=2000)

print(probability)

hat1=Hat(black=6,red=4,green=3)
probability=experiment(hat=hat1,expected_balls={"red":2,"green":1},num_balls_drawn=5,num_experiment=2000)

print(probability)



