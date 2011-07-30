## Strawberry Fields

## Common steps for all solvers

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

