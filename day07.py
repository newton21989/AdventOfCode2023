import os

WILDCARD = "J"

cardValues = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
if WILDCARD is not "":
  newValues = []
  newValues.append(WILDCARD)
  for card in cardValues:
    if card is not WILDCARD:
      newValues.append(card)

  cardValues = newValues

HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE_OF_A_KIND = 3
FULL_HOUSE = 4
FOUR_OF_A_KIND = 5
FIVE_OF_A_KIND = 6

def arrMax(arr):
  for i, element in enumerate(arr):
    if i == 0:
      out = element
    else:
      out = max(out, element)
    pos = i

  return out, pos

def arrCount(arr, value):
  count = 0
  for element in arr:
    if element == value:
      count += 1

  return count

def getHandType(hand):
  counts = [0,0,0,0,0,0,0,0,0,0,0,0,0]
  for card in hand:
    for i, check in enumerate(cardValues):
      if card == check:
        counts[i] += 1

  pairs = arrCount(counts, 2)
  maxCount, card = arrMax(counts)

  if(WILDCARD is not ""):
    wildCount = counts[0]

  if wildCount == 0:
    if maxCount == 1:
      out = HIGH_CARD
    elif maxCount == 2 and pairs == 1:
      out = ONE_PAIR
    elif maxCount == 2 and pairs == 2:
      out = TWO_PAIR
    elif maxCount == 3 and pairs == 0:
      out = THREE_OF_A_KIND
    elif maxCount == 3 and pairs == 1:
      out = FULL_HOUSE
    elif maxCount == 4:
      out = FOUR_OF_A_KIND
    elif maxCount == 5:
      out = FIVE_OF_A_KIND
    else:
      raise ValueError("Unable to determine hand type")
  elif wildCount > 0:
    if maxCount == 1 and wildCount == 1:
      out = ONE_PAIR
    elif maxCount == 2 and wildCount == 1 and pairs == 1:
      out = THREE_OF_A_KIND
    elif maxCount == 2 and wildCount == 1 and pairs == 2:
      out = FULL_HOUSE
    elif maxCount == 2 and wildCount == 2 and pairs == 1:
      out = THREE_OF_A_KIND
    elif maxCount == 2 and wildCount == 2 and pairs == 2:
      out = FOUR_OF_A_KIND
    elif maxCount == 3 and wildCount == 1:
      out = FOUR_OF_A_KIND
    elif maxCount == 3 and wildCount == 2:
      out = FIVE_OF_A_KIND
    elif maxCount == 3 and wildCount == 3 and pairs == 0:
      out = FOUR_OF_A_KIND
    elif maxCount == 3 and wildCount == 3 and pairs == 1:
      out = FIVE_OF_A_KIND
    elif maxCount == 4 or wildCount == 4 or wildCount == 5:
      out = FIVE_OF_A_KIND
    else:
      raise ValueError("Unable to determine hand type")
  else:
    raise ValueError("Number of wildcards not >= 0")

  return out

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

if __name__ == "__main__":
  filename = './day07-input.txt'

  if not os.path.isfile(filename):
    raise FileExistsError("Error: input file does not exist.")
  else:
    with open(filename, 'r') as f:
      read = f.read().rstrip()
      lines = read.splitlines(0)
      f.close()

  print(f"Wildcard: {WILDCARD if WILDCARD is not '' else 'none'}")
  print(f"Answer: {part1(sortHands(lines))}")
