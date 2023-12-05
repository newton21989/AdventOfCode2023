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
  matches = re.findall(r"(one|two|three|four|five|six|seven|eight|nine)", numberString)
  while matches.__len__() > 0:
    match = matches.pop(0)
    if match == "one":
      num = "1"
    elif match == "two":
      num = "2"
    elif match == "three":
      num = "3"
    elif match == "four":
      num = "4"
    elif match == "five":
      num = "5"
    elif match == "six":
      num = "6"
    elif match == "seven":
      num = "7"
    elif match == "eight":
      num = "8"
    elif match == "nine":
      num = "9"

    numberString = re.sub(match, num, numberString, 1)
  
  return numberString

def getData(string):
  match = re.findall(r"(\d)|(\d)", string)
  firstDigit = match[0][0]
  if(match.__len__() > 1):
    secondDigit = match[match.__len__() - 1][0]
  else:
    secondDigit = match[0][0]

  return f"{firstDigit}{secondDigit}"

def getTotal(lines):
  total = 0
  for line in lines:
    line = numStrReplace(line)
    strData = getData(line)

    intNum = int(strData)
    total += intNum

  return total

print(f"Total = {getTotal(lines)}")
