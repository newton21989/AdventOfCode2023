import day01
import pytest

def test_replace_number():
  assert day01.numStrReplace("1") == "1"

def test_replace_string():
  assert day01.numStrReplace("one") == "1"

def test_dont_replace_string():
  with pytest.raises(ValueError):
    day01.numStrReplace("oneleven")

def test_dont_total():
  assert day01.getTotal("mt") == 0

def test_overlapping_match():
  assert day01.getTotal(["oneight"]) == 18

def test_leading_noise():
  assert day01.getTotal(["pppmfmnfourtworxrqrfhbgx8vvxgrjzhvqmztltwo"]) == 42

def test_add_string_numbers():
  assert day01.getTotal(["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]) == 281
 #assert day01.getTotal(["29","83","13","24","42","14","76"]) == 281
