## Strawberry Fields

import common
import s0

import copy
import doctest
import itertools
import sys
import time

def backtracking_search(puzzle, width = 3):
  """
  backtracking_search produces a solution to <puzzle>.

  It works by exploring all paths through the solution space where the diff
  after a join is the lowest. This is basically the same as simple_reduction
  but it doesn't commit to the first path it encounters.

  >>> solve("p3.text") # doctest: +ELLIPSIS
  71
  ...
  """
  max, field = puzzle

  solution = (sys.maxint, None)

  paths = [(common.cost(field), field), ]
  while len(paths) > 0:
    curr_cost, field = paths.pop(0)

    # figure out the current number of greenhouses
    greenhouses = common.ids(field)

    diffs = {}
    # try each combination of greenhouses
    for g1, g2 in itertools.combinations(greenhouses, 2):
      # find outer bounds (left, right, top and bottom) for a greenhouse made
      # up of g1 and g2
      size1, p11, p12 = common.outer_bounds(g1, field)
      size2, p21, p22 = common.outer_bounds(g2, field)
      size3, p31, p32 = common.outer_bounds([g1, g2], field)

      if size3 is not None:
        diff = size3 - size2 - size1
        if diff not in diffs.keys():
          diffs[diff] = [(g1, g2),]
        else:
          diffs[diff].append((g1, g2))

    # find the list of joins which has the least diff, perform each join
    # in a fresh copy of field and add it to paths if cost is lower than
    # current cost, otherwise compare cost to solution and either discard
    # this path or replace solution.
    if len(diffs.keys()) > 0:
      _paths = diffs[sorted(diffs.keys())[0]]
      for (g1, g2) in _paths[0:width]:
        _field = common.join(g1, g2, copy.deepcopy(field))
        if common.cost(_field) < curr_cost:
          paths.append((common.cost(_field), _field))

        if common.cost(_field) < solution[0] and \
           len(greenhouses) <= max + 1:

          solution = (common.cost(_field), _field)

  return max, solution[1]

def solve(filename):
  """
  solve prints out solutions to each of the fields described in <filename>.
  """
  count, total = 0, 0
  for puzzle in common.parse_file(filename):
    max, field = backtracking_search(s0.join_vertically(s0.join_horizontally(s0.identify(puzzle))))

    count += 1
    total += common.cost(field)
    print common.cost(field)
    print common.format(field)

  print "%s field(s). Total cost is $%s" % (count, total)

if __name__ == "__main__":
  doctest.testmod()
  doctest.testfile("tests.text")

  if len(sys.argv[1:]) > 0:
    for f in sys.argv[1:]:
      solve(f)


