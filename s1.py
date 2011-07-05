## Strawberry Fields

import doctest

def solve1(puzzle):
  """
  solve1 identifies all strawberries and proposes a simplistic "solution".

  The solution may or may not work depending on the number of strawberries
  in the field and the max number of greenhouses.

  >>> solve1((1, ['.@@.', '.@@.', '.@@.']))
  [[0, 1, 2, 0], [0, 3, 4, 0], [0, 5, 6, 0]]

  >>> solve1((1, ['@..', '.@.', '..@']))
  [[1, 0, 0], [0, 2, 0], [0, 0, 3]]

  >>> solve1((1, ['@@@@@@', '@@@@@@', '@@@@@@', '@@@@@@', '@@@@@@']))
  [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30]]
  """
  import string

  max, field = puzzle
  id = 1

  result = []
  for line in field:
    _line = []
    for c in line:
      if c == "@":
        _line.append(id)
        id += 1
      else:
        _line.append(0)

    result.append(_line)

  return result
      

def parse_file(filename):
  """
  parse_file reads a puzzle input file and returns a list of puzzle details.

  puzzle details are represented as a tuple containing the maximum number of
  greenhouses and a list of strings representing the field.
  """
  f = open(filename, "r")

  result = []
  max, field = None, []
  for line in f.readlines():
    line = line.strip()
    if line == "":
      if max is not None:
        result.append((max, field))
        max, field = None, []
    elif max is None:
      max = int(line)
    else:
      field.append(line)

  if max is not None:
    result.append((max, field))

  f.close()

  return result 

if __name__ == "__main__":
  doctest.testmod()
  doctest.testfile("tests.text")
