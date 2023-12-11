import os

filename = './day08-input.txt'

if not os.path.isfile(filename):
  raise FileExistsError("Error: input file does not exist.")
else:
  with open(filename, 'r') as f:
    read = f.read().rstrip()
    lines = read.splitlines(0)
    f.close()

instructions = lines.pop(0)
lines.pop(0)

def parseData(lines):
  m = []
  for line in lines:
    firstSplit = line.split(' = (')
    secondSplit = firstSplit[1].split(', ')

    m.append([firstSplit[0], secondSplit[0], secondSplit[1][:3]])

  return m
  
def traverse(map):
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

    if nextHop == "ZZZ":
      break

    thisHop = [x for x, el in enumerate(map) if nextHop in el[0]][0]

  return hops

print(f"Part 1: {traverse(parseData(lines))}")
