import nose
from gaussrand import gaussrand

def test_gaussrand():
	"""Test the function gaussrand."""
	u = gaussrand()
	v = gaussrand()
	assert u != v
	
if __name__=='__main__':
	nose.runmodule()
