import nose
from coords import polar_to_cartesian

def test_coord1():
	assert polar_to_cartesian(-4,120,2) == "(2.00, -3.46)"

def test_coord2():
	assert polar_to_cartesian(1,180,3) == "(-1.000, 0.000)"
	
def test_coord3():
	assert polar_to_cartesian(-1,360,0) == "(-1, 0)"
	
def test_coord4():
	assert polar_to_cartesian(2,90,1) == "(0.0, 2.0)"
	
if __name__ == "__main__":
	nose.runmodule()
