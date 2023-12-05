import day01

def test_replace_string():
  assert day01.numStrReplace("1one1") == "111"

def test_replace_repeated_string():
  assert day01.numStrReplace("1one1one") == "1111"

def test_dont_replace_string():
  assert day01.numStrReplace("oneeleven1") == "1eleven1"

def test_overlapping_match():
  assert day01.numStrReplace("xtwone3four") == "x2ne34"

def test_replace_every_string():
  assert day01.numStrReplace("onextwoxthreexfourxfivexsixxsevenxeightxnine") == "1x2x3x4x5x6x7x8x9"

def test_extract_data():
  assert day01.getData("1337") == "17"

def test_extract_noisier_data():
  assert day01.getData("one3threellama7lol") == "37"

def test_add_string_numbers():
  assert day01.getTotal(["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]) == 281
