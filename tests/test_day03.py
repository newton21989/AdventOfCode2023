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

def test_find_gear_numbers():
  assert day03.findGearNumbers(test_data.splitlines(0)) == [[467, 35],[755,598]]

def test_part_2_test_data():
  assert day03.findGearRatios(test_data.splitlines(0)) == 467835

def test_part_2_more_test_data():
  assert day03.findGearRatios(more_test_data.splitlines(0)) == 829928

def test_find_number_from_start():
  assert day03.getNumberFromCoords(test_data.splitlines(0), 0, 5) == 114

def test_find_number_from_middle():
  assert day03.getNumberFromCoords(test_data.splitlines(0), 2, 8) == 633

def test_find_number_from_end():
  assert day03.getNumberFromCoords(test_data.splitlines(0), 4, 2) == 617

