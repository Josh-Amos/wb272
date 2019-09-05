import nose
from temperature import to_celcius

def test_to_celcius():
	"""Test the function to_celcius."""
	assert to_celcius(32) == 0
	pass

if __name__ == '__main__':
	nose.runmodule()
