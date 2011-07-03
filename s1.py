## Strawberry Fields

## Strawberries are growing in a rectangular field of length and width at most
## 50. You want to build greenhouses to enclose the strawberries. Greenhouses
## are rectangular, axis-aligned with the field (i.e., not diagonal), and may
## not overlap. The cost of each greenhouse is $10 plus $1 per unit of area
## covered.

## Write a program that chooses the best number of greenhouses to build, and
## their locations, so as to enclose all the strawberries as cheaply as
## possible. Heuristic solutions that may not always produce the lowest
## possible cost will be accepted: seek a reasonable tradeoff of efficiency
## and optimality.

## Your program must read a small integer 1 <= N <= 10 representing the maximum
## number of greenhouses to consider, and a matrix representation of the field,
## in which the '@' symbol represents a strawberry. Output must be a copy of
## the original matrix with letters used to represent greenhouses, preceded by
## the covering's cost. Here is an example input-output pair:

## Input:
## 4
## ..@@@@@...............
## ..@@@@@@........@@@...
## .....@@@@@......@@@...
## .......@@@@@@@@@@@@...
## .........@@@@@........
## .........@@@@@........

## Output:
## 90
## ..AAAAAAAA............
## ..AAAAAAAA....CCCCC...
## ..AAAAAAAA....CCCCC...
## .......BBBBBBBCCCCC...
## .......BBBBBBB........
## .......BBBBBBB........

## In this example, the solution cost of $90 is computed as (10+8*3) + (10+7*3)
## + (10+5*3).

## Run your program on the 9 sample inputs found in this file and report the
## total cost of the 9 solutions found by your program, as well as each
## individual solution.

import doctest

def parse_file(filename):
  """
  parse_file reads a puzzle input file and returns a list of puzzle details.

  puzzle details are represented as a tuple containing the maximum number of
  greenhouses and a list of strings representing the field.

  >>> f = open("*doctest*parse_file*", "w")
  >>> f.write("4\\n.@@.\\n.@@.\\n..@.")
  >>> f.close()
  >>> parse_file("*doctest*parse_file*")
  [(4, ['.@@.', '.@@.', '..@.'])]

  >>> f = open("*doctest*parse_file*", "w")
  >>> f.write("4\\n.@@.\\n.@@.\\n..@.\\n\\n3\\n.@@.\\n.@@.\\n..@.")
  >>> f.close()
  >>> parse_file("*doctest*parse_file*")
  [(4, ['.@@.', '.@@.', '..@.']), (3, ['.@@.', '.@@.', '..@.'])]

  >>> f = open("*doctest*parse_file*", "w")
  >>> f.write("4\\n.@@.\\n.@@.\\n..@.\\n\\n\\n3\\n.@@.\\n.@@.\\n..@.")
  >>> f.close()
  >>> parse_file("*doctest*parse_file*")
  [(4, ['.@@.', '.@@.', '..@.']), (3, ['.@@.', '.@@.', '..@.'])]
  """
  f = open(filename, "r")

  result = []
  max, field = None, []
  for line in f.readlines():
    line = line.strip()
    if max is None:
      max = int(line)
    elif line.strip() == "":
      result.append((max, field))
      max, field = None, []
    else:
      field.append(line)

  if max is not None:
    result.append((max, field))

  f.close()

  return result 

if __name__ == "__main__":
  doctest.testmod()
