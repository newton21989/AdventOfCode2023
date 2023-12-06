import day03

test_data = """467..114..
...*......
..35...633
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

more_test_data = \
"""..124..#......&.....
...........602...932
.................*..
..431.....3.....889.
....%.....*.........
...........460..904."""

def test_part_1_test_data():
  assert day03.findPartNumber(test_data.splitlines(0)) == 4361

def test_single_digit():
  assert day03.findPartNumber(more_test_data.splitlines(0)) == 3317
