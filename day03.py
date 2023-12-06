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

def findPartNumber(data):
  number = ""
  countIt = False
  total = 0

  for lineNum, line in enumerate(data):
    for col, char in enumerate(line):
      if char in ('0','1','2','3','4','5','6','7','8','9'):
        number += char
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
          s = data[lineNum - 1][col]
        except IndexError:
          s = "."

        try:
          se = data[lineNum + 1][col + 1]
        except IndexError:
          se = "."

        adjacent = [nw, n, ne, w, e, sw, s, se]

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
