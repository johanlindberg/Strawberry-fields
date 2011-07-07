## Strawberry Fields

import doctest

def solve3(puzzle):
  """
  solve3 reduces the number of greenhouses further.

  solve3 enforces the max constraint but can reduce the number even further
  if that would end up with a lower overall cost.

  >>> solve3((1, [[1, 2, 0, 0], [0, 3, 4, 0], [0, 0, 5, 6]]))
  [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
  """
  pass

def solve2(puzzle):
  """
  solve2 reduces the number of greenhouses by joining adjacent ones.

  solve2 does not care about the max constraint, it does not care about the
  cost of greenhouses. It merely joins greenhouses the lie next to each other.
  The only constraint it enforces is that greenhouses have to be rectangular. 

  XXX This function needs some refactoring. It is too complex!
  """
  max, field = puzzle
  
  # join greenhouses horizontally
  for r in xrange(len(field)):
    for c in xrange(len(field[r]) - 1):
      if field[r][c] > 0 and \
         field[r][c+1] > 0 and \
         field[r][c] != field[r][c+1]:

        field[r][c+1] = field[r][c]

  # join greenhouses vertically
  for r in xrange(len(field) - 1):
    start, stop = -1, -1
    for c in xrange(len(field[r]) - 1):
      if field[r][c] > 0:
        if start == -1:
          start = c
        elif field[r][c] != field[r][c+1] or \
             ( field[r][c] == field[r][c+1] and c+1 == len(field[r]) - 1 ):

          stop = c
          if field[r][c] == field[r][c+1] and \
             c+1 == len(field[r]) - 1:
            
            stop += 1

          # if we end up here we've found a chain of greenhouses
          # if we find a similar chain in the row below we join
          # them, otherwise we leave them as they are (for now)
          
          if start == 0 or \
             field[r+1][start-1] != field[r+1][start]:

            if stop == len(field[r]) - 1 or \
               field[r+1][stop+1] != field[r+1][stop]:

              join = True
              i = start
              while i < stop:
                if field[r+1][i] == 0 or \
                   field[r+1][i] != field[r+1][i+1]:

                  join = False
                  break
            
                i += 1
          
              if join:
                while start <= stop:
                  field[r+1][start] = field[r][start]

                  start += 1

          start, stop = -1, -1

  return field

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
