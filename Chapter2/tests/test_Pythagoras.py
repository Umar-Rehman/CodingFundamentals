from src import Pythagoras

def test_find_Side():
    newPyth = Pythagoras.Pythagoras(5,4)
    assert newPyth.find_Side() == 3

def test_find_Hyp():
    newPyth = Pythagoras.Pythagoras(3,4)
    assert newPyth.find_Hyp() == 5
