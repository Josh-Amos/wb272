import nose
from rock_paper_scissors import winner

def test01():
    """Test 1"""
    p1 = "R"
    p2 = "R"
    assert winner(p1,p2) == "It's a Draw"

def test02():
    """Test 2"""
    assert winner("R","S") == "Player 1 wins"

def test03():
    """Test 3"""
    assert winner("R","P") == "Player 2 wins"

def test04():
    """Test 4""" 
    assert winner("P","P") == "It's a Draw"

def test05():
    """Test 5""" 
    assert winner("P","R") == "Player 1 wins"

def test06():
    """Test 6""" 
    assert winner("P","S") == "Player 2 wins"

def test07():
    """Test 7""" 
    assert winner("S","S") == "It's a Draw"

def test08():
    """Test 8""" 
    assert winner("S","R") == "Player 2 wins"

def test09():
    """Test 9""" 
    assert winner("S","P") == "Player 1 wins"

if __name__ == "__main__":
    nose.runmodule()
    
