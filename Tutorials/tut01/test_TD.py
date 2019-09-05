import nose
from TDuration import elapsed_minutes

def test_D1():
	assert elapsed_minutes("0800","1930") == 690

def test_D2():
	assert elapsed_minutes("1532","2359") == 507

def test_D3():
	assert elapsed_minutes("0338","2054") == 1036

def test_D4():
	assert elapsed_minutes("1955","2312") == 197	
	
def test_D5():
	assert elapsed_minutes("0531","1424") == 533

if __name__ == "__main__":
	nose.runmodule()
