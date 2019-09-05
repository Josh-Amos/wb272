import nose
from TTemperature import f2c

def test_temp1():
	"""Tests temp1"""
	assert f2c(387,4) == "197.2222"

def test_temp2():
	"""Tests temp2"""
	assert f2c(2967,3) == "1630.556"

def test_temp3():
	"""Tests temp3"""
	assert f2c(-77,1) == "-60.6"
	
def test_temp4():
	"""Tests temp4"""
	assert f2c(-987,2) == "-566.11"

def test_absZero():
	"""Tests absolute zero"""
	assert f2c(-459.67,2) == "-273.15"

def test_Parity():
	"""Tests Parity"""
	assert f2c(-40,1) == "-40.0"

def test_Zero():
	"""Tests Zero"""
	assert f2c(0,2) == "-17.78"

def test_Freezing():
	"""Tests Freezing point"""
	assert f2c(32,0) == "0"

def test_BodyTemp():
	"""Tests Body Temperature"""
	assert f2c(98.6,0) == "37"

def test_Boiling():
	"""Tests boiling point"""
	assert f2c(212,0) == "100" 


if __name__ == "__main__":
	nose.runmodule()
