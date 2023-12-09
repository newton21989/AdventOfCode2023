import os

filename = './day03-input.txt'

if not os.path.isfile(filename):
  print("Error: input file does not exist.")
  exit
else:
  with open(filename, 'r') as f:
    read = f.read().rstrip()
    lines = read.splitlines(0)
    f.close()

def scanAdjacent(data, lineNum, col):
  try:
    nw = data[lineNum - 1][col - 1]
  except IndexError:
    nw = "."

  try:
    n = data[lineNum - 1][col]
  except IndexError:
    n = "."

  try:
    ne = data[lineNum - 1][col + 1]
  except IndexError:
    ne = "."

  try:
    w = data[lineNum][col - 1]
  except IndexError:
    w = "."

  try:
    e = data[lineNum][col + 1]
  except IndexError:
    e = "."

  try:
    sw = data[lineNum + 1][col - 1]
  except IndexError:
    sw = "."

  try:
    s = data[lineNum + 1][col]
  except IndexError:
    s = "."

  try:
    se = data[lineNum + 1][col + 1]
  except IndexError:
    se = "."

  return [nw, n, ne, w, e, sw, s, se]

def getNumberFromCoords(data, lineNum, col):
  i = 0
  number = ""
  while True:
    try:
      test = data[lineNum][col - i]
    except:
      break
    
    if data[lineNum][col - i] in ("1","2","3","4","5","6","7","8","9","0"):
      number = data[lineNum][col - i] + number
      i += 1
    else:
      break

  i = 1
  while True:
    try:
      test = data[lineNum][col + i]
    except:
      break
    
    if data[lineNum][col + i] in ("1","2","3","4","5","6","7","8","9","0"):
      number = number + data[lineNum][col + i]
      i += 1
    else:
      break

  return int(number)

def findGearNumbers(data):
  numberses = []

  for lineNum, line in enumerate(data):
    for col, char in enumerate(line):
      if char == "*":
        adjacent = scanAdjacent(data, lineNum, col)

        numbers = []
        mapNum = []
        mapBool = []
        for i, j in enumerate(adjacent):
          try:
            mapNum.append(int(j))
            mapBool.append(True)
          except:
            mapNum.append(-1)
            mapBool.append(False)

        if(mapBool[1]):
          numbers.append(getNumberFromCoords(data, lineNum - 1, col))
        else:
          if(mapBool[0]):
            numbers.append(getNumberFromCoords(data, lineNum - 1, col - 1))
          if(mapBool[2]):
            numbers.append(getNumberFromCoords(data, lineNum - 1, col + 1))

        if(mapBool[6]):
          numbers.append(getNumberFromCoords(data, lineNum + 1, col))
        else:
          if(mapBool[5]):
            numbers.append(getNumberFromCoords(data, lineNum + 1, col - 1))
          if(mapBool[7]):
            numbers.append(getNumberFromCoords(data, lineNum + 1, col + 1))

        if(mapBool[3]):
          numbers.append(getNumberFromCoords(data, lineNum, col - 1))
        if(mapBool[4]):
          numbers.append(getNumberFromCoords(data, lineNum, col + 1))

        if(numbers.__len__() > 1):
          numberses.append(numbers)

  return numberses

def findGearRatios(data):
  sum = 0
  gearNumbers = findGearNumbers(data)
  for gear in gearNumbers:
    product = 0
    for i, number in enumerate(gear):
      if(i == 0):
        product = number
      else:
        product = product * number
    sum += product

  return sum

def findPartNumber(data):
  number = ""
  countIt = False
  total = 0

  for lineNum, line in enumerate(data):
    for col, char in enumerate(line):
      if char in ('0','1','2','3','4','5','6','7','8','9'):
        number += char

        adjacent = scanAdjacent(data, lineNum, col)

        if not countIt:
          for adjChar in adjacent:
            if adjChar in ("`","~","!","@","#","$","%","^","&","*","(",")","-","=","_","+","{","}","[","]","/","?","\\","|","<",">",",",":",";","\"","'"):
              countIt = True
              break

        if adjacent[4] in ("1","2","3","4","5","6","7","8","9","0"):
          continue
        else:
          if countIt:
            total += int(number)

          number = ""
          countIt = False

  return total

print(f"Part 1: {findPartNumber(lines)}")
print(f"Part 2: {findGearRatios(lines)}")
