import day09

test_data = \
"""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

def test_fill_tree():
  assert day09.fillTree([[0,3,6,9,12,15]]) == [[0,3,6,9,12,15],[3,3,3,3,3],[0,0,0,0]]

def test_reverse_tree():
  assert day09.reverseTree([[0,3,6,9,12,15],[3,3,3,3,3],[0,0,0,0]]) == [[0,3,6,9,12,15,18],[3,3,3,3,3,3],[0,0,0,0]]

def test_extrapolate():
  assert day09.extrapolate("0 3 6 9 12 15") == 18

def test_part_1_test_data():
  assert day09.part_1(test_data.splitlines(0)) == 114
