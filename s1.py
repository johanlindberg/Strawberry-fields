## Strawberry Fields

import doctest

def solve2(puzzle):
  """
  solve2 reduces the number of greenhouses by joining adjacent ones.

  >>> solve2((1, [[0, 1, 2, 0], [0, 3, 4, 0], [0, 5, 6, 0]]))
  [[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]
  """
  pass

def solve1(puzzle):
  """
  solve1 identifies all strawberries and proposes a simplistic "solution".

  The solution is basically to propose one greenhouse/strawberry. This may
  or may not work depending on the number of strawberries in the field and
  the max number of greenhouses.
  """
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
