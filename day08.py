import os
import numpy as np
from threading import Thread
from time import sleep

instructions = ""

def parseData(lines):
  global instructions, data
  instructions = lines.pop(0)
  lines.pop(0)
  m = []
  for line in lines:
    firstSplit = line.split(' = (')
    secondSplit = firstSplit[1].split(', ')

    m.append([firstSplit[0], secondSplit[0], secondSplit[1][:3]])

  return m

def traverseInTandem(map):
  startingPoints = [x for x, el in enumerate(map) if el[0].endswith("A")]
  hops = []
  for start in startingPoints:
    hops.append(np.int64(traverse(map, start)))

  lcm = np.lcm.reduce(hops)
  return lcm

def traverse(map, start = -1):
  if start == -1:
    start = [x for x, el in enumerate(map) if "AAA" in el[0]][0]

  thisHop = start
  i = 0
  hops = 0
  while True:
    hops += 1
    instruction = instructions[i]
    if instruction == "L":
      nextHop = map[thisHop][1]
    elif instruction == "R":
      nextHop = map[thisHop][2]

    if i == instructions.__len__() - 1:
      i = 0
    else:
      i += 1

    if nextHop.endswith("Z"):
      break

    thisHopMk1 = [x for x, el in enumerate(map) if nextHop in el[0]]
    thisHop = thisHopMk1[0]

  return hops

if __name__ == "__main__":
  filename = './day08-input.txt'

  if not os.path.isfile(filename):
    raise FileExistsError("Error: input file does not exist.")
  else:
    with open(filename, 'r') as f:
      read = f.read().rstrip()
      lines = read.splitlines(0)
      f.close()


  data = parseData(lines)
  print(f"Part 1: {traverse(data)}")
  print(f"Part 2: {traverseInTandem(data)}")
