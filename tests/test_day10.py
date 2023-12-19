import day10

test_data = \
"""7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""

def test_get_start():
  assert day10.getStart(test_data.splitlines(0)) == [2, 0]

def test_part_1_test_data():
  day10.setData(test_data.splitlines(0))
  assert day10.part_1(test_data.splitlines(0)) == 8
