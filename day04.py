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

def arrSum(array):
  sum = 0
  for element in array:
    sum += element

  return sum

def getMatches(card):
  numbers = card.split('|')
  winningNums = numbers[0].split(' ')
  myNums = numbers[1].split(' ')

  matches = 0
  for num in myNums:
    if num != "" and num in winningNums:
      matches += 1

  return matches

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

def getTotalMatches(data):
  cardCopies = [1] * data.__len__()
  total = 0
  for lineNum, line in enumerate(data):
    cardMatches = getMatches(line)
    for i in range(lineNum + 1, lineNum + cardMatches + 1):
      for j in range(1, cardCopies[lineNum] + 1):
        cardCopies[i] += 1
    
  total = arrSum(cardCopies)
  
  return total

print(f"Part 1: {getTotal(lines)}")
print(f"Part 2: {getTotalMatches(lines)}")
