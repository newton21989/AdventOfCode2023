import os
import re

filename = './day03-test-data.txt'

if not os.path.isfile(filename):
  print("Error: input file does not exist.")
  exit
else:
  with open(filename, 'r') as f:
    read = f.read().rstrip()
    lines = read.splitlines(0)
    f.close()

number = ""
countIt = False
total = 0

for lineNum, line in enumerate(lines):
  for col, char in enumerate(line):
    if char in ('0','1','2','3','4','5','6','7','8','9'):
      number += char
      adjacent = [
        lines[lineNum - 1][col - 1],
        lines[lineNum - 1][col    ],
        lines[lineNum - 1][min(col + 1, line.__len__() - 1)],
        lines[lineNum    ][col - 1],
        lines[lineNum    ][min(col + 1, line.__len__() - 1)],
        lines[min(lineNum + 1, lines.__len__() - 1)][col - 1],
        lines[min(lineNum + 1, lines.__len__() - 1)][col    ],
        lines[min(lineNum + 1, lines.__len__() - 1)][min(col + 1, line.__len__() - 1)]
      ]

      for adjChar in adjacent:
        if adjChar in ("`","~","!","@","#","$","%","^","&","*","(",")","-","=","_","+","{","}","[","]","\\","|","<",">",",",":",";","\"","'"):
          countIt = True
          break

      if adjacent[4] in ("1","2","3","4","5","6","7","8","9","0","\0"):
        continue
      else:
        if countIt:
          total += int(number)

        number = ""
        countIt = False

print(f"Part 1: {total}")
