## Strawberry Fields

import doctest
import itertools
import string
import sys

def ids(field):
  """
  ids returns a list of greenhouse identities in <field>.
  """
  ids = []
  for row in field:
    for col in row:
      if col > 0 and \
         col not in ids:

        ids.append(col)

  return ids

def cost(field):
  """
  cost calculates the total cost of all greenhouses in <field>.
  """
  greenhouses = ids(field)

  cost = 0
  for g in greenhouses:
    size, _, _ = outer_bounds(g, field)
    cost += 10 + size

  return cost

def join(g1, g2, field):
  """
  join expands greenhouse <g1> in <field> until it contains <g2>.
  """
  _, (l,t), (r,b) = outer_bounds([g1, g2], field)
  for ri in xrange(len(field)):
    for ci in xrange(len(field[ri])):
      if ci >= l and \
         ci <= r and \
         ri >= t and \
         ri <= b:

        field[ri][ci] = g1

  return field

def outer_bounds(gi, field):
  """
  outer_bounds returns the size and coordinates of the box(es) in <gi>.

  <gi> can be a list or an int. If it is a list it returns the size and
  coordinates of the box that contains all boxes specified in <gi>.
  """ 
  if not isinstance(gi, list):
    gi = [gi,]

  l, r, t, b = 50, -1, 50, -1 # default values = max size of field

  for ri in xrange(len(field)):
    for ci in xrange(len(field[ri])):
      cell = field[ri][ci]
      if cell in gi:
        if l > ci: l = ci
        if r < ci: r = ci
        if t > ri: t = ri
        if b < ri: b = ri

  size = (r-l+1) * (b-t+1)
  return size, (l,t), (r,b)

def solve4(puzzle):
  """
  solve4 reduces the number of greenhouses until max constraint is met.
  """
  max, field = puzzle

  # figure out the current number of greenhouses
  greenhouses = ids(field)

  # join greenhouses until max constraint is met
  while len(greenhouses) > max:
    j1, j2, js = 0, 0, sys.maxint
    # try each combination of greenhouses
    for g1, g2 in itertools.combinations(greenhouses, 2):
      # find outer bounds (left, right, top and bottom) for a greenhouse made
      # up of g1 and g2
      size1, p11, p12 = outer_bounds(g1, field)
      size2, p21, p22 = outer_bounds(g2, field)
      size3, p31, p32 = outer_bounds([g1, g2], field)

      diff = size3 - size2 - size1
      if diff < js:
        j1, j2, js = g1, g2, diff

    # join j1 and j2, remove j2 from greenhouses
    field = join(j1, j2, field)
    greenhouses.remove(j2)

  return max, field

def solve2(puzzle):
  """
  solve2 reduces the number of greenhouses by joining horizontally adjacent ones.

  solve2 does not care about the max constraint and it does not care about the
  cost of greenhouses. It merely joins greenhouses that lie next to each other.
  """
  max, field = puzzle
  
  # join greenhouses horizontally

  hz_segments = []
  # find the horizontal border segments
  for ri in xrange(len(field)):
    for ci in xrange(len(field[ri]) - 1):
      if ( field[ri][ci] == 0 and \
           field[ri][ci+1] > 0 ) or \
         ( field[ri][ci] > 0 and \
           field[ri][ci+1] == 0 ):

        if not ci+1 in hz_segments:
          hz_segments.append(ci+1)

  # join greenhouses
  for ri in xrange(len(field)):
    for ci in xrange(len(field[ri]) - 1):
      if field[ri][ci] > 0 and \
         field[ri][ci+1] > 0 and \
         field[ri][ci] != field[ri][ci+1]:

        if ci+1 not in hz_segments:
          field[ri][ci+1] = field[ri][ci]

  return max, field

def solve3():
  """
  XXX TBD!
  """
  # join greenhouses vertically
  for ri in xrange(len(field) - 1):
    start, stop = -1, -1
    for ci in xrange(len(field[ri]) - 1):
      if field[ri][ci] > 0:
        if start == -1:
          start = ci
        elif field[ri][ci] != field[ri][ci+1] or \
             ( field[ri][ci] == field[ri][ci+1] and ci+1 == len(field[ri]) - 1 ):

          stop = ci
          if field[ri][ci] == field[ri][ci+1] and \
             ci+1 == len(field[ri]) - 1:
            
            stop += 1

          # if we end up here we've found a chain of greenhouses
          # if we find a similar chain in the row below we join
          # them, otherwise we leave them as they are (for now)
          
          if start == 0 or \
             field[ri+1][start-1] != field[ri+1][start]:

            if stop == len(field[ri]) - 1 or \
               field[ri+1][stop+1] != field[ri+1][stop]:

              join = True
              i = start
              while i < stop:
                if field[ri+1][i] == 0 or \
                   field[ri+1][i] != field[ri+1][i+1]:

                  join = False
                  break
            
                i += 1
          
              if join:
                while start <= stop:
                  field[ri+1][start] = field[ri][start]

                  start += 1

          start, stop = -1, -1

  return max, field

def solve1(puzzle):
  """
  solve1 identifies all strawberries and proposes a simplistic "solution".

  The solution is basically to propose one greenhouse/strawberry. This may
  or may not work depending on the number of strawberries in the field and
  the max number of greenhouses.
  """
  max, field = puzzle
  id = 1

  _field = []
  for row in field:
    _row = []
    for c in row:
      if c == "@":
        _row.append(id)
        id += 1
      else:
        _row.append(0)

    _field.append(_row)

  return max, _field 

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

def solve(filename):
  """
  solve prints out solutions to each of the fields described in <filename>.
  """
  for puzzle in parse_file(filename):
#    max, field = solve3(solve2(solve1(puzzle)))
    max, field = solve2(solve1(puzzle))

    print cost(field)

    # prepare field for printing
    ng = iter(string.uppercase)
    greenhouses = ids(field)
    for g in greenhouses:
      gid = ng.next()
      for ri in xrange(len(field)):
        for ci in xrange(len(field[ri])):
          if field[ri][ci] == 0:
            field[ri][ci] = "."
          elif field[ri][ci] == g:
            field[ri][ci] = gid

    for row in field:
      print "".join(row)

    print

if __name__ == "__main__":
  doctest.testmod()
  doctest.testfile("tests.text")

  if len(sys.argv[1:]) > 0:
    for f in sys.argv[1:]:
      solve(f)


