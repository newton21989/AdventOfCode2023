import os
import re

filename = './day01-input.txt'

if not os.path.isfile(filename):
  print("Error: input file does not exist.")
  exit
else:
  with open(filename, 'r') as f:
    read = f.read().rstrip()
    lines = read.splitlines(0)
    f.close()

def numStrReplace(numberString):
  try: 
    int(numberString) != 0
    return numberString
  except ValueError as e:
    if numberString == "one":
      num = "1"
    elif numberString == "two":
      num = "2"
    elif numberString == "three":
      num = "3"
    elif numberString == "four":
      num = "4"
    elif numberString == "five":
      num = "5"
    elif numberString == "six":
      num = "6"
    elif numberString == "seven":
      num = "7"
    elif numberString == "eight":
      num = "8"
    elif numberString == "nine":
      num = "9"
    else:
      raise ValueError("Input could not be interpreted as number")

  return num

def getTotal(lines):
  total = 0
  for line in lines:
    matchFirst = re.findall(r"(\d|one|two|three|four|five|six|seven|eight|nine)", line, re.MULTILINE)
    matchLast = re.findall(r".*(\d|one|two|three|four|five|six|seven|eight|nine).{0,}$", line, re.MULTILINE)

    strData = "0"
    if matchFirst.__len__() > 0:
      matchFirst = matchFirst[0]
      matchLast = matchLast[0]

      strData = numStrReplace(matchFirst) + numStrReplace(matchLast)

    intNum = int(strData)
    total += intNum

  return total

print(f"Total = {getTotal(lines)}")
