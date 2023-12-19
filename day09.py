import os
import numpy as np
from threading import Thread
from time import sleep

lines = []

def getDiffs(values):
  diff = []
  for i in range(0, len(values) - 1):
    diff.append(values[i + 1] - values[i])

  return diff

def fillTree(tree):
  i = 0
  while True:
    diff = getDiffs(tree[i])
    tree.append(diff)
    nonZeros = [x for x in diff if x != 0]

    if len(nonZeros) > 0:
      i += 1
      continue
    else:
      break
  return tree

def reverseTree(tree):
  for i in range(len(tree) - 2, -1, -1):
    branch1 = tree[i]
    branch2 = tree[i + 1]

    num1 = branch1[len(branch1) - 1]
    num2 = branch2[len(branch2) - 1]
    branch1.append(num1 + num2)
    tree[i] = branch1

  return tree

def extrapolate(line):
  values = line.split(' ')
  tree = []

  intVals = []
  for v in values:
    intVals.append(int(v))

  tree.append(intVals)

  fillTree(tree)
  reverseTree(tree)

  return tree[0][len(tree[0]) - 1]

def part_1(lines):
  total = 0

  for line in lines:
    total += extrapolate(line)

  return total

def parseData(data):
  global lines
  lines = data.splitlines(0)

if __name__ == "__main__":
  filename = './day09-input.txt'

  if not os.path.isfile(filename):
    raise FileExistsError("Error: input file does not exist.")
  else:
    with open(filename, 'r') as f:
      read = f.read().rstrip()
      f.close()

  parseData(read)

  print(f"Part 1: {part_1(lines)}")
