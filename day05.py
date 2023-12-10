import os

filename = './day05-input.txt'

if not os.path.isfile(filename):
  raise FileExistsError("Error: input file does not exist.")
  exit
else:
  with open(filename, 'r') as f:
    read = f.read().rstrip()
    f.close()

seeds = []
seedToSoil= []
soilToFert = []
fertToWater = []
waterToLight = []
lightToTemp = []
tempToHum = []
humToLoc = []

def arrMin(array):
  out = 65535
  for num, element in enumerate(array):
    if num == 0:
      out = element
    elif element < out:
      out = element

  return out


def getSeeds(data):
  seeds = data.split(' ')
  intSeeds = []

  for i, seed in enumerate(seeds):
    try:
      intSeeds.append(int(seed))
    except ValueError:
      continue
  
  return intSeeds

def getMap(data):
  lines = data.splitlines(0)
  lines.pop(0)
  m = []
  for line in lines:
    vals = line.split(' ')
    destStart = int(vals[0])
    srcStart = int(vals[1])
    r = int(vals[2])

    for i in range(0, r):
      m.append([srcStart + i, destStart + i])

  return m


def parseData(data):
  global seeds, seedToSoil, soilToFert, fertToWater, waterToLight, lightToTemp, tempToHum, humToLoc

  dataSections = data.split("\n\n")

  for section in dataSections:
    if section.startswith("seeds"):
      seeds = getSeeds(section)
    elif section.startswith("seed-to-soil"):
      seedToSoil = getMap(section)
    elif section.startswith("soil-to-fert"):
      soilToFert = getMap(section)
    elif section.startswith("fertilizer-to-water"):
      fertToWater = getMap(section)
    elif section.startswith("water-to-light"):
      waterToLight = getMap(section)
    elif section.startswith("light-to-temp"):
      lightToTemp = getMap(section)
    elif section.startswith("temperature-to-humidity"):
      tempToHum = getMap(section)
    elif section.startswith("humidity-to-location"):
      humToLoc = getMap(section)

def unmap(source, map):
  dest = -1
  for x in map:
    if x[0] == source:
      dest = x[1]
      break

  if dest == -1:
    dest = source

  return dest

def lookup(seed):
  global seedToSoil, soilToFert, fertToWater, waterToLight, lightToTemp, tempToHum, humToLoc

  soil = unmap(seed, seedToSoil)
  fert = unmap(soil, soilToFert)
  water = unmap(fert, fertToWater)
  light = unmap(water, waterToLight)
  temp = unmap(light, lightToTemp)
  hum = unmap(temp, tempToHum)
  loc = unmap(hum, humToLoc)

  return loc

def part1():
  locs = []
  for seed in seeds:
    locs.append(lookup(seed))

  return arrMin(locs)

parseData(read)

print(f"Part 1: {part1()}")
