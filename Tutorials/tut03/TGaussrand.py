import random
import math

def gauss():
	u = random.random()
	v = random.random()
	return math.sin(2 * math.pi * v) * math.sqrt(-2 * math.log(u))
