import day07

test_data = \
"""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

def test_arr_max():
  assert day07.arrMax([3,1,4,2]) == 4

def test_get_hand_type():
  assert day07.getHandType("32T3K") == 2

def test_get_card_value():
  assert day07.getCardValue("A") == 12

def test_get_tie_breaker():
  assert day07.getTieBreaker("QQQKQ", "QQKQQ") == "QQKQQ"

def test_comp_hands():
  assert day07.compHand("32T3K", "T55J5") == "T55J5"

def test_sort_hands():
  assert day07.sortHands(test_data.splitlines(0)) == ["32T3K 765", "KTJJT 220", "KK677 28", "T55J5 684", "QQQJA 483"]

def test_part_1_test_data():
  assert day07.part1(day07.sortHands(test_data.splitlines(0))) == 6440
