This repository is mainly to hold some vacation python hacking on an ITA
Software puzzle. Nothing to see here. Move along. At the time of writing this
puzzle can be found at [ITA Software's career page](http://www.itasoftware.com/careers/work-at-ita/hiring-puzzles.html)

Strawberry fields
-----------------

Strawberries are growing in a rectangular field of length and width at most 50.
You want to build greenhouses to enclose the strawberries. Greenhouses are
rectangular, axis-aligned with the field (i.e., not diagonal), and may not
overlap. The cost of each greenhouse is $10 plus $1 per unit of area covered.

Write a program that chooses the best number of greenhouses to build, and their
locations, so as to enclose all the strawberries as cheaply as possible.
Heuristic solutions that may not always produce the lowest possible cost will be
accepted: seek a reasonable tradeoff of efficiency and optimality.

Your program must read a small integer 1 <= N <= 10 representing the maximum
number of greenhouses to consider, and a matrix representation of the field, in
which the '@' symbol represents a strawberry. Output must be a copy of the
original matrix with letters used to represent greenhouses, preceded by the
covering's cost. Here is an example input-output pair:

    Input
    4
    ..@@@@@...............
    ..@@@@@@........@@@...
    .....@@@@@......@@@...
    .......@@@@@@@@@@@@...
    .........@@@@@........
    .........@@@@@........
   
    Output
    90
    ..AAAAAAAA............
    ..AAAAAAAA....CCCCC...
    ..AAAAAAAA....CCCCC...
    .......BBBBBBBCCCCC...
    .......BBBBBBB........
    .......BBBBBBB........

In this example, the solution cost of $90 is computed as (10+8*3) + (10+7*3) +
(10+5*3).