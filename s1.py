## Strawberry Fields

import doctest

def solve1(puzzle):
  """
  solve1 identifies all strawberries and proposes a simplistic solution.

  >>> solve1((1, ['.@@.', '.@@.', '.@@.']))
  ['.AA.', '.AA.', '.AA.']
  """
  max, field = puzzle
  result = []
  for line in field:
    _line = []
    for c in line:
      if c == "@":
        _line += "A"
      else:
        _line += c

    result.append("".join(_line))

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
