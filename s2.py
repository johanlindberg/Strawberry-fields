## Strawberry Fields

import common
import s0

import copy
import doctest
import itertools
import sys
import time

def backtracking_search(puzzle):
  """
  backtracking_search produces a solution to <puzzle>.

  It works by exploring all paths through the solution space where the diff
  after a join is the lowest. This is basically the same as simple_reduction
  but it doesn't commit to the first path it encounters.
  """
  pass

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


