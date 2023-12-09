import os
import re

filename = './day04-input.txt'

if not os.path.isfile(filename):
  raise FileExistsError("Error: input file does not exist.")
  exit
else:
  with open(filename, 'r') as f:
    read = f.read().rstrip()
    lines = read.splitlines(0)
    f.close()

def getCard(line):
  numbers = line.split('|')
  winningNums = numbers[0].split(' ')
  myNums = numbers[1].split(' ')

  score = 0
  for num in myNums:
    if num != "" and num in winningNums:
      if(score == 0):
        score = 1
      else:
        score += score

  return score

def getTotal(data):
  total = 0
  for line in data:
    cardScore = getCard(line)
    total += cardScore

  return total

print(f"Part 1: {getTotal(lines)}")
