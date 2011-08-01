## Strawberry Fields

import common
import s0

import copy
import doctest
import itertools
import sys
import time

# Helpers

def unrotate(field):
  """
  unrotate undo the effects of rotate on <field>.
  """
  return flip_hz(flip_vt(rotate(field)))

def rotate(field):
  """
  rotates <field> 90 degrees.
  """
  result = []

  # make the resulting structure
  width, height = len(field[0]), len(field)
  row = [0] * height
  for w in xrange(width):
    result.append(copy.deepcopy(row))

  # copy data from field to result
  for ri in xrange(len(field)):
    field[ri].reverse()
    for ci in xrange(len(field[ri])):
      result[ci][ri] = field[ri][ci]

  return result

def flip_vt(field):
  """
  flip_vt flips <field> vertically.
  """
  field.reverse()
  return field

def flip_hz(field):
  """
  flip_hz flips <field> horizontally.
  """
  result = []
  for row in field:
    row.reverse()
    result.append(row)

  return result

def variant_reduction(puzzle):
  """
  variant_reduction flips and rotates <puzzle> to find a better solution.
  """
  max, field = puzzle
  
  # there are 8 variations to each puzzle, these 4 + 4 rotated ones
  variants = [lambda f: f, lambda f: flip_hz(f), lambda f: flip_vt(f), lambda f: flip_vt(flip_hz(f))]
  rotated_field = rotate(copy.deepcopy(field))

  best_cost, best_field = sys.maxint, None
  for vi in xrange(4):
    _, _field = simple_reduction((max, variants[vi](copy.deepcopy(field))))
    if common.cost(_field) < best_cost:
      best_cost, best_field = common.cost(_field), variants[vi](_field)

    _, _field = simple_reduction((max, variants[vi](copy.deepcopy(rotated_field))))
    if common.cost(_field) < best_cost:
      best_cost, best_field = common.cost(_field), unrotate(variants[vi](_field))

  return max, best_field

def simple_reduction(puzzle):
  """
  simple_reduction returns a solution to <puzzle>.

  It works by reducing the number of greenhouses one by one until it has the
  lowest cost and meets the max constraint.
  """
  max, field = puzzle

  # figure out the current number of greenhouses
  greenhouses = common.ids(field)

  # we need to keep a copy of the previous field and it's cost in order
  # to return it once we've realized we've done one reduction too many
  prev_field, prev_cost = None, sys.maxint
  if len(greenhouses) <= max:
    prev_field, prev_cost = copy.deepcopy(field), common.cost(field)

  # join greenhouses until when run out of them or until max constraint
  # is met *and* cost increases from one reduction to the next
  while len(greenhouses) > 1:
    j1, j2, js = 0, 0, sys.maxint
    # try each combination of greenhouses
    for g1, g2 in itertools.combinations(greenhouses, 2):
      # find outer bounds (left, right, top and bottom) for a greenhouse made
      # up of g1 and g2
      size1, p11, p12 = common.outer_bounds(g1, field)
      size2, p21, p22 = common.outer_bounds(g2, field)
      size3, p31, p32 = common.outer_bounds([g1, g2], field)

      if size3 is not None:
        diff = size3 - size2 - size1
        if diff < js:
          j1, j2, js = g1, g2, diff

    # if we run out of combinations to try
    # we must either surrender (return None)
    # or if len(greenhouses) <= max return
    # the best solution we have.
    if j1 == 0:
      if len(greenhouses) <= max:
        return max, prev_field
      else:
        return max, None

    # join j1 and j2, remove j2 from greenhouses
    field = common.join(j1, j2, field)
    greenhouses.remove(j2)

    # decide if we should exit this loop or keep on reducing
    curr_cost = common.cost(field)
    if len(greenhouses) < max:
      if prev_cost < curr_cost:
        return max, prev_field

    prev_field, prev_cost = copy.deepcopy(field), curr_cost

  # if we end up here, we've come down to 1 greenhouse
  return max, field

def solve(filename):
  """
  solve prints out solutions to each of the fields described in <filename>.
  """
  count, total = 0, 0
  for puzzle in common.parse_file(filename):
    max, field = variant_reduction(s0.join_vertically(s0.join_horizontally(s0.identify(puzzle))))

    count += 1
    total += common.cost(field)
    print common.cost(field)
    print common.format(field)

  print "%s field(s). Total cost is $%s" % (count, total)

if __name__ == "__main__":
  if len(sys.argv[1:]) == 0:
    print "Running doctests."
    doctest.testmod()
    doctest.testfile("tests.text")
  else:
    for f in sys.argv[1:]:
      solve(f)


