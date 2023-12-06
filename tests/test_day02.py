import day02
import pytest

test_data = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

def test_game_is_possible():
  assert day02.getGameIsPossible("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == True

def test_game_is_not_possible():
  assert day02.getGameIsPossible("8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red") == False

def test_get_game_fewest():
  assert day02.getGameFewest("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == 48

def test_part_1_test_data():
  assert day02.getTotal(test_data) == 8

def test_part_2_test_data():
  assert day02.getTotalPower(test_data) == 2286
