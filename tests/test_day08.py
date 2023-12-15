import day08

test_data = \
"""LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

test_data_2 = \
"""LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

def test_part_1_test_data():
  day08.parseData(test_data)
  assert day08.traverse() == 6

def test_part_2_test_data():
  day08.parseData(test_data)
  assert day08.traverseInTandem() == 6
