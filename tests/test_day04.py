import day04

test_data = \
"""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def test_card_1():
  assert day04.getCard(test_data.splitlines(0)[0]) == 8

def test_d4p1_test_data():
  assert day04.getTotal(test_data.splitlines(0)) == 13
  
def test_count_matches():
  assert day04.getMatches(test_data.splitlines(0)[0]) == 4

def test_total_matches():
  assert day04.getTotalMatches(test_data.splitlines(0)) == 30
