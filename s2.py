## Strawberry Fields

import common
import s0
import s1

import copy
import doctest
import itertools
import sys
import time

def simple_reduction_search(puzzle, width = 2):
  """
  simple_reduction_search produces a solution to <puzzle>.

  It works by exploring all choices through the solution space where the diff
  after a join is the lowest. It uses s1.simple_reduction as a heuristic to
  decide on which path to commit to. 

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
      __costs = {}
      for (g1, g2) in _paths[0:width]:
        _field = common.join(g1, g2, copy.deepcopy(field))
        _, __field = s1.simple_reduction((max, copy.deepcopy(_field)))
        cf = common.cost(__field)
        if cf < curr_cost:
          if cf not in __costs.keys():
            __costs[cf] = [_field,]
          else:
            __costs[cf].append(_field)

      # find the list of fields with the least cost and add them to the
      # list of paths to explore
      if len(__costs.keys()) > 0:
        c = sorted(__costs.keys())[0]
        __paths = __costs[c]
        for f in __paths:
          cf = common.cost(f)
          paths.append((cf, f))

          if cf < solution[0] and \
             len(common.ids(f)) <= max:

            solution = (cf, f)

  return max, solution[1]

def solve(filename):
  """
  solve prints out solutions to each of the fields described in <filename>.
  """
  count, total = 0, 0
  for puzzle in common.parse_file(filename):
    max, field = simple_reduction_search(s0.join_vertically(s0.join_horizontally(s0.identify(puzzle))))

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


