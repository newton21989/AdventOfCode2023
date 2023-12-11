import os

filename = './day07-input.txt'

if not os.path.isfile(filename):
  raise FileExistsError("Error: input file does not exist.")
else:
  with open(filename, 'r') as f:
    read = f.read().rstrip()
    lines = read.splitlines(0)
    f.close()

cardValues = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def arrMax(arr):
  for i, element in enumerate(arr):
    if i == 0:
      out = element
    else:
      out = max(out, element)

  return out

def getHandType(hand):
  counts = [0,0,0,0,0,0,0,0,0,0,0,0,0]
  for card in hand:
    for i, check in enumerate(cardValues):
      if card == check:
        counts[i] += 1

  return arrMax(counts)

def getCardValue(card):
  global cardValues
  for i in range(len(cardValues) - 1, -1, -1):
    if card == cardValues[i]:
      return i
    
  raise ValueError("Card value not found")

def getTieBreaker(hand1, hand2):
  for i in range(0, 5):
    if hand1[i] == hand2[i]:
      continue
      
    v1 = getCardValue(hand1[i])
    v2 = getCardValue(hand2[i])
    if v1 > v2:
      return hand1
    elif v1 < v2:
      return hand2
    
  raise ValueError("Neither hand is stronger.")

def compHand(hand1, hand2):
  t1 = getHandType(hand1)
  t2 = getHandType(hand2)
  if t1 > t2:
    return hand1
  elif t1 < t2:
    return hand2
  else:
    return getTieBreaker(hand1, hand2)

def sortHands(lines):
  for j in range(0, lines.__len__() - 1):
    for i in range(0, lines.__len__() - j - 1):
      line1 = lines[i]
      line2 = lines[i + 1]
      hand1 = line1.split(' ')[0]
      hand2 = line2.split(' ')[0]

      comp = compHand(hand1, hand2)
      if comp == hand1:
        lines[i] = line2
        lines[i + 1] = line1

  return lines

def part1(sortedHands):
  total = 0
  for i, hand in enumerate(sortedHands):
    bid = int(hand.split(' ')[1])
    total += (i + 1) * bid
  
  return total

print(f"Part 1: {part1(sortHands(lines))}")
