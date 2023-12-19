import os

lines = []
NORTH = 11
WEST = 12
EAST = 13
SOUTH = 14

class Cursor:
  def __init__(self, pos):
    self.pos = pos

  def getChar(self):
    return lines[self.pos[0]][self.pos[1]]
  
  def getDirection(self):
    return self.direction
  
  def goNextDirection(self):
    if self.direction == NORTH:
      if self.getChar() == "7":
        self.goWest()
      elif self.getChar() == "|":
        self.goNorth()
      elif self.getChar() == "F":
        self.goEast()
      else:
        raise ValueError("Could not find direction")
    elif self.direction == WEST:
      if self.getChar() == "L":
        self.goNorth()
      elif self.getChar() == "-":
        self.goWest()
      elif self.getChar() == "F":
        self.goSouth()
      else:
        raise ValueError("Could not find direction")
    elif self.direction == EAST:
      if self.getChar() == "J":
        self.goNorth()
      elif self.getChar() == "-":
        self.goEast()
      elif self.getChar() == "7":
        self.goSouth()
      else:
        raise ValueError("Could not find direction")
    elif self.direction == SOUTH:
      if self.getChar() == "J":
        self.goWest()
      elif self.getChar() == "|":
        self.goSouth()
      elif self.getChar() == "L":
        self.goEast()
      else:
        raise ValueError("Could not find direction")
    else:
      raise ValueError("Could not find direction")

  def goNorth(self):
    self.pos[0] += -1
    self.direction = NORTH

  def goSouth(self):
    self.pos[0] += 1
    self.direction = SOUTH

  def goEast(self):
    self.pos[1] += 1
    self.direction = EAST

  def goWest(self):
    self.pos[1] += -1
    self.direction = WEST

def getConnectsN(char):
  if char in ("7", "|", "F"):
    return True
  else:
    return False

def getConnectsW(char):
  if char in ("L", "-", "F"):
    return True
  else:
    return False

def getConnectsE(char):
  if char in ("J", "-", "7"):
    return True
  else:
    return False

def getConnectsS(char):
  if char in ("L", "|", "J"):
    return True
  else:
    return False

def scanAdjacent(data, lineNum, col):
  try:
    n = data[lineNum - 1][col]
  except IndexError:
    n = "."

  try:
    w = data[lineNum][col - 1]
  except IndexError:
    w = "."

  try:
    e = data[lineNum][col + 1]
  except IndexError:
    e = "."

  try:
    s = data[lineNum + 1][col]
  except IndexError:
    s = "."

  return [n, w, e, s]

def getStart(lines):
  for lineNum, line in enumerate(lines):
    try:
      col = line.index("S")
      return [lineNum, col]
    except ValueError:
      continue

def part_1(lines):
  loc = getStart(lines)
  cur = Cursor(loc)

  n,w,e,s = scanAdjacent(lines, loc[0], loc[1])
  if getConnectsN(n):
    cur.goNorth()
  elif getConnectsW(w):
    cur.goWest()
  elif getConnectsE(e):
    cur.goEast()
  elif getConnectsS(s):
    cur.goSouth()
  else:
    raise ValueError("Could not find direction")
  
  hops = 1
  while cur.getChar() != "S":
    hops += 1
    cur.goNextDirection()

  return int(hops / 2)

def setData(data):
  global lines
  lines = data

if __name__ == "__main__":
  filename = './day10-input.txt'

  if not os.path.isfile(filename):
    raise FileExistsError("Error: input file does not exist.")
  else:
    with open(filename, 'r') as f:
      read = f.read().rstrip()
      lines = read.splitlines(0)
      f.close()

  print(f"Part 1: {part_1(lines)}")
