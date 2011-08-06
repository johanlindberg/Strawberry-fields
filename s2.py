## Strawberry Fields

import common
import s0
import s1

import copy
import doctest
import itertools
import sys
import time

def search(puzzle, breakpoint = 2):
  """
  search produces a solution to <puzzle>.

  >>> solve("p3.text") # doctest: +ELLIPSIS
  71
  ...
  """
  max, field = puzzle

  solution = (common.cost(field), field)

  paths = [solution, ]
  while len(paths) > 0:
    curr_cost, field = paths.pop(0)

    # Figure out the current number of greenhouses
    greenhouses = common.ids(field)

    if len(greenhouses) > 1:
      diffs = {}
      # Try each combination of greenhouses
      for g1, g2 in itertools.combinations(greenhouses, 2):
        # Find outer bounds (left, right, top and bottom) for a greenhouse made
        # up of g1 and g2
        size3, p31, p32 = common.outer_bounds([g1, g2], field)

        if size3 is not None:
          size1, p11, p12 = common.outer_bounds(g1, field)
          size2, p21, p22 = common.outer_bounds(g2, field)

          diff = size3 - size2 - size1
          if diff not in diffs.keys():
            diffs[diff] = [(g1, g2),]
          else:
            diffs[diff].append((g1, g2))

      # Find the list of joins which has the lowest diff and select the joins
      # of the most frequent greenhouse.
      if len(diffs.keys()) > 0:
        freqs = {}
        for (g1, g2) in diffs[sorted(diffs.keys())[0]]:
          if g1 not in freqs.keys():
            freqs[g1] = [(g1, g2),]
          else:
            freqs[g1].append((g1, g2))

          if g2 not in freqs.keys():
            freqs[g2] = [(g1, g2),]
          else:
            freqs[g2].append((g1, g2))

        # Perform each join in a fresh copy of field and add it to paths if
        # cost is lower than current cost, otherwise compare cost to solution
        # and either discard this path or add it as best-so-far.
        joins = freqs[sorted(freqs.keys(), key = lambda k: len(freqs[k]), reverse = True)[0]]
        if len(joins) <= breakpoint:
          (g1, g2) = joins[0]
          _, _field = s1.simple_reduction((max, common.join(g1, g2, copy.deepcopy(field))))

          cf = common.cost(_field)
          if cf < solution[0] and \
             len(common.ids(_field)) <= max:

            solution = (cf, _field)

        else:
          for (g1, g2) in joins:
            _field = common.join(g1, g2, copy.deepcopy(field))
            cf = common.cost(_field)
            if cf < curr_cost:
              paths.append((cf, _field))

              if cf < solution[0] and \
                 len(common.ids(_field)) <= max:

                solution = (cf, _field)

  return max, solution[1]

def solve(filename):
  """
  solve prints out solutions to each of the fields described in <filename>.
  """
  tstart = time.time()
  count, total = 0, 0
  for puzzle in common.parse_file(filename):
    pstart = time.time()
    max, field = search(s0.join_vertically(s0.join_horizontally(s0.identify(puzzle))))

    count += 1
    total += common.cost(field)
    print "cost:", common.cost(field), "time:", time.strftime("%H:%M:%S", time.gmtime(time.time() - pstart))
    print common.format(field)

  print "%s field(s). Total cost is $%s" % (count, total)
  print time.strftime("Total time is %H:%M:%S", time.gmtime(time.time() - tstart))

if __name__ == "__main__":
  if len(sys.argv[1:]) == 0:
    print "Running doctests."
    doctest.testmod()
    doctest.testfile("tests.text")
  else:
    for f in sys.argv[1:]:
      solve(f)


