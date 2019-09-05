import TGaussrand
import nose

def test_TGaussrand():
	"""A function that checks whether two values are randomly generated"""
	u = TGaussrand.gauss()
	v = TGaussrand.gauss()
	assert u != v
	
if __name__ =="__main__":
	nose.runmodule()
