## Strawberry Fields

import copy
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

  for ri in xrange(t, b+1):
    for ci in xrange(l, r+1):
      if field[ri][ci] > 0 and \
         field[ri][ci] not in gi:
        return None, (l,t), (r,b)

  size = (r-l+1) * (b-t+1)
  return size, (l,t), (r,b)

def simple_search(puzzle):
  """
  simple_search reduces the number of greenhouses until max constraint is met.
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

      if size3 is not None:
        diff = size3 - size2 - size1
        if diff < js:
          j1, j2, js = g1, g2, diff

    # join j1 and j2, remove j2 from greenhouses
    field = join(j1, j2, field)
    greenhouses.remove(j2)

  return max, field

def join_horizontally(puzzle):
  """
  join_horizontally reduces the number of greenhouses by joining adjacent ones.

  join_horizontally does not care about the max constraint and it does not care
  about the cost of greenhouses. It merely joins greenhouses that lie next to
  each other.
  """
  max, field = puzzle
  
  segments = []
  # find the horizontal border segments
  for ri in xrange(len(field)):
    for ci in xrange(len(field[ri]) - 1):
      if ( field[ri][ci] == 0 and \
           field[ri][ci+1] > 0 ) or \
         ( field[ri][ci] > 0 and \
           field[ri][ci+1] == 0 ):

        if not ci+1 in segments:
          segments.append(ci+1)

  # join greenhouses
  for ri in xrange(len(field)):
    for ci in xrange(len(field[ri]) - 1):
      if field[ri][ci] > 0 and \
         field[ri][ci+1] > 0 and \
         field[ri][ci] != field[ri][ci+1]:

        if ci+1 not in segments:
          field[ri][ci+1] = field[ri][ci]

  return max, field

def join_vertically(puzzle):
  """
  join_vertically reduces the number of greenhouses by joining vertically adjacent ones.

  It is basically the same function as join_horizontally.
  """
  max, field = puzzle
  
  segments = []
  # find the vertical border segments
  for ci in xrange(len(field[0])):
    for ri in xrange(len(field) - 1):
      if ( field[ri][ci] == 0 and \
           field[ri+1][ci] > 0 ) or \
         ( field[ri][ci] > 0 and \
           field[ri+1][ci] == 0 ):

        if not ri+1 in segments:
          segments.append(ri+1)

  # join greenhouses
  for ci in xrange(len(field[0])):
    for ri in xrange(len(field) - 1):
      if field[ri][ci] > 0 and \
         field[ri+1][ci] > 0 and \
         field[ri][ci] != field[ri+1][ci]:

        if ri+1 not in segments:
          field[ri+1][ci] = field[ri][ci]

  return max, field

def identify(puzzle):
  """
  Identifies and enumerates all strawberries.
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

def format(_field):
  """
  format makes a string representation of field suitable for printing.
  """
  field = copy.deepcopy(_field)
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

  result = ""
  for row in field:
    result += "".join(row) + "\n"

  return result

def solve(filename):
  """
  solve prints out solutions to each of the fields described in <filename>.
  """
  for puzzle in parse_file(filename):
    max, field = simple_search(join_vertically(join_horizontally(identify(puzzle))))

    print cost(field)
    print format(field)

if __name__ == "__main__":
  doctest.testmod()
  doctest.testfile("tests.text")

  if len(sys.argv[1:]) > 0:
    for f in sys.argv[1:]:
      solve(f)


