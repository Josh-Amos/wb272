import nose
from temperature import c2f

def test_freezing():
    """Test freezing point of water"""
    x = c2f(0)
    epis = pow(10,-15)
    assert abs(x - 32) < epis

def test_boiling():
    """Test boiling point of water"""
    x = c2f(100)
    epis = pow(10,-15)
    assert abs(x - 212) < epis
    
def test_body():
    """Test normal body temperature"""
    x = c2f(37)
    epis = pow(10,-15)
    assert abs(x - 98.6) < epis
    
def test_fever():
    """Test temperature of fever"""
    x = c2f(340/9)
    epis = pow(10,-15)
    assert abs(x - 100) < epis

if __name__ == '__main__':
   nose.runmodule()
