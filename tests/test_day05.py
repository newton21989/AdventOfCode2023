import day05

test_data = \
"""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

test_data_short = \
"""seeds: 42 55 27 38

test-to-test map:
22 55 2
87 90 4"""

def test_get_seeds():
  assert day05.getSeeds(test_data.split("\n\n")[0]) == [79,14,55,13]

def test_parse_map():
  assert day05.getMap(test_data_short.split("\n\n")[1]) == [[22, 55, 2], [87, 90, 4]]

def test_unmap():
  day05.parseData(test_data)
  assert day05.unmap(79, day05.seedToSoil) == 81

def test_seed_to_loc_lookup():
  day05.parseData(test_data)
  assert day05.lookup(79) == 82

def test_part_1_test_data():
  day05.parseData(test_data)
  assert day05.part1() == 35

# def test_part_2_test_data():
#   day05.parseData(test_data)
#   assert day05.part2() == 46
