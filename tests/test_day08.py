import day08

test_data = \
"""LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

def test_part_1_test_data():
  data = test_data.splitlines(0)
  instructions = data.pop(0)
  data.pop(0)
  assert day08.traverse(data) == 6
