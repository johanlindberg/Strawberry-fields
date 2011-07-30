## Strawberry Fields

import copy
import string
import sys

## Common helper functions for all solvers

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
  if field is None:
    return sys.maxint

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

