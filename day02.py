import os
import re

filename = './day02-input.txt'

if not os.path.isfile(filename):
  print("Error: input file does not exist.")
  exit
else:
  with open(filename, 'r') as f:
    read = f.read().rstrip()
    lines = read.splitlines(0)
    f.close()

def getGameIsPossible(gameData):
  rounds = gameData.split(';')
  for round in rounds:
    matchReds = re.findall(r"(\d+)\ red", round, re.MULTILINE)
    matchGreens = re.findall(r"(\d+)\ green", round, re.MULTILINE)
    matchBlues = re.findall(r"(\d+)\ blue", round, re.MULTILINE)

    if matchReds.__len__() > 0:
      countReds = int(matchReds[0])
    else:
      countReds = 0

    if matchGreens.__len__() > 0:
      countGreens = int(matchGreens[0])
    else:
      countGreens = 0

    if matchBlues.__len__() > 0:
      countBlues = int(matchBlues[0])
    else:
      countBlues = 0

    if countReds > 12:
      return False
    
    if countGreens > 13:
      return False
    
    if countBlues > 14:
      return False
    
  return True

def getGameFewest(gameData):
  rounds = gameData.split(';')
  minReds = 0
  minGreens = 0
  minBlues = 0
  for round in rounds:
    matchReds = re.findall(r"(\d+)\ red", round, re.MULTILINE)
    matchGreens = re.findall(r"(\d+)\ green", round, re.MULTILINE)
    matchBlues = re.findall(r"(\d+)\ blue", round, re.MULTILINE)

    if matchReds.__len__() > 0:
      minReds = max(int(matchReds[0]), minReds)
    
    if matchGreens.__len__() > 0:
      minGreens = max(int(matchGreens[0]), minGreens)
    
    if matchBlues.__len__() > 0:
      minBlues = max(int(matchBlues[0]), minBlues)
    
  power = minReds * minGreens * minBlues
  return power


def getTotal(lines):
  total = 0
  for line in lines:
    matchGame = re.findall(r"^Game\ (\d+):\ (.*)$", line, re.MULTILINE)

    gameId = matchGame[0][0]
    gameData = matchGame[0][1]

    if(getGameIsPossible(gameData)):
      total += int(gameId)

  return total

def getTotalPower(lines):
  total = 0
  for line in lines:
    matchGame = re.findall(r"^Game\ (\d+):\ (.*)$", line, re.MULTILINE)

    gameData = matchGame[0][1]

    total += getGameFewest(gameData)

  return total

print(f"Part 1: {getTotal(lines)}")
print(f"Part 2: {getTotalPower(lines)}")
