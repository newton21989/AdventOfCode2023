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

total = 0

for line in lines:
  match = re.findall(r"^\D*(\d)|.*(\d).*$", line)
  firstDigit = match[0][0]
  if(match.__len__() > 1):
    secondDigit = match[1][1]
  else:
    secondDigit = match[0][0]

  strNum = f"{firstDigit}{secondDigit}"

  intNum = int(strNum)
  total += intNum

print(f"Total = {total}")
