from src import TimeCalculator, base

def test_sort_time():
    times="01:25:65"
    newtimes = times.split(":")
    newtimes = list(map(int, newtimes))
    TC = TimeCalculator.TimeCalculator()
    assert TC.sort_time(newtimes) == [2, 2, 5]

def test_add():
    li = [[2, 2, 5], [2, 6, 40]]
    TC = TimeCalculator.TimeCalculator(li)
    assert TC.add() == "04:08:45"
    
def test_difference():
    li = [[4, 8, 45], [2, 6, 40]]
    TC = TimeCalculator.TimeCalculator(li)
    assert TC.difference() == "02:02:05"

def test_convert_to_hours():
    li = [[2, 2, 5]]
    TC = TimeCalculator.TimeCalculator(li)
    assert TC.convert_to_hours() == 50.08

def test_convert_to_mins():
    li = [[1, 0, 0]]
    TC = TimeCalculator.TimeCalculator(li)
    assert TC.convert_to_mins() == 1440

def test_convert_mins_to_time():
    base.set_keyboard_input(["1440"])
    TC = TimeCalculator.TimeCalculator()
    assert TC.convert_mins_to_time() == "01:00:00"

def test_convert_hours_to_time():
    base.set_keyboard_input(["24"])
    TC = TimeCalculator.TimeCalculator()
    assert TC.convert_hours_to_time() == "01:00:00"

def test_convert_days_to_time():
    base.set_keyboard_input(["1"])
    TC = TimeCalculator.TimeCalculator()
    assert TC.convert_days_to_time() == "01:00:00"

def test_get_times():
    base.set_keyboard_input(["01:26:75"])
    assert TimeCalculator.get_times() == [[2, 3, 15]]

def test_calculate_time():
    base.set_keyboard_input(["8"])
    assert TimeCalculator.calculate_time() == None