from TDays import day_of_the_week
import nose
import calendar

def test_Day1():
	assert day_of_the_week(1940,12,31) == 2

def test_Day2():
	assert day_of_the_week(2057,5,3) == calendar.weekday(2057,5,3) + 1  
	
def test_Day3():
	assert day_of_the_week(2018,10,30) == 2

def test_Day4():
	assert day_of_the_week(2200,7,14) == calendar.weekday(2200,7,14) + 1

def test_Day5():
	assert day_of_the_week(2002,11,29) == calendar.weekday(2002,11,29) + 1

def test_Day6():
	assert day_of_the_week(1976,6,16) == calendar.weekday(1976,6,16) + 1

def test_Day7():
	assert day_of_the_week(1912,1,1) == calendar.weekday(1912,1,1) + 1

if __name__ == "__main__":
	nose.runmodule()
