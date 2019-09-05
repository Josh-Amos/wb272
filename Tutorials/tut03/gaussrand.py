import random
import math

def gaussrand():
	u = random.random()
	v = random.random()
	
	p1 = math.sin(2 * math.pi * v)
	p2 = math.sqrt(-2*math.log(u))
	
	w = p1 * p2
	
	return w
	
 	
