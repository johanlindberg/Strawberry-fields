This repository is mainly to hold some vacation python hacking on an ITA
Software puzzle.

Nothing to see here... Move along.

At the time of writing this puzzle can be found at [ITA Software's career page](http://www.itasoftware.com/careers/work-at-ita/hiring-puzzles.html)

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

Run your program on the 9 sample inputs found in [this file](https://github.com/johanlindberg/Strawberry-fields/blob/master/rectangles.txt) and report the total
cost of the 9 solutions found by your program, as well as each individual
solution.

Results
-------

Here are the results for the example puzzle given in the problem description ([p1.text](https://github.com/johanlindberg/Strawberry-fields/blob/master/p1.text)).

Both solvers arrive at $90 as total cost.

    > python2.6 s1.py p1.text
    cost: 90 time: 00:00:00
    ..AAAAAAAA............
    ..AAAAAAAA......BBB...
    ..AAAAAAAA......BBB...
    .......CCCCCCCCCBBB...
    .......CCCCCCCCC......
    .......CCCCCCCCC......

    1 field(s). Total cost is $90
    Total time is 00:00:00

    > python2.6 s2.py p1.text 
    cost: 90 time: 00:00:04
    ..AAAAAAAA............
    ..AAAAAAAA......BBB...
    ..AAAAAAAA......BBB...
    .......CCCCCCCCCBBB...
    .......CCCCCCCCC......
    .......CCCCCCCCC......

    1 field(s). Total cost is $90
    Total time is 00:00:04

Here are the results for [rectangles.txt](https://github.com/johanlindberg/Strawberry-fields/blob/master/rectangles.txt).

The second solver finds a $12 better solution to puzzle #3 ([p3.text](https://github.com/johanlindberg/Strawberry-fields/blob/master/p3.text)) but spends a lot more run time to do so. Most of that time is spent on the last puzzle, unfortunately it still misses the better solution of $364 (see [strawberry.txt](https://github.com/sunilnandihalli/strawberry-fields/blob/master/strawberry.txt#L287))

    > python2.6 s1.py rectangles.txt
    cost: 41 time: 00:00:00
    .............
    .............
    .............
    ...AAAA......
    ...AAAA......
    ...AAAA......
    .......BBB...
    .......BBB...
    .......BBB...
    .............
    
    cost: 62 time: 00:00:00
    .............
    ..AAAAAA.....
    ..AAAAAA.....
    ..AAAAAA.....
    ..AAAAAA.....
    ..AAAAAA.....
    ..AAAAAA.....
    ..........BBB
    ..........BBB
    
    cost: 83 time: 00:00:00
    .........A...
    .........A...
    BBBCCCCCCA...
    BBB......A...
    BBB......A...
    BBB......A...
    BBBDDDDDDDDDD
    BBB..........
    BBB..........
    
    cost: 181 time: 00:00:03
    .........................
    ..AAAAAAAAAAAAAAAAAAAA...
    ..AAAAAAAAAAAAAAAAAAAA...
    ..BB.................C...
    ..BB.................C...
    ..BB.......DDD.......C.E.
    ..BB.......DDD.......C...
    ..BB...FFFFDDDGGGGGGGC...
    ..BB...FFFFDDDGGGGGGGC...
    ..BB.......DDD.......C...
    ..BB.......DDD.......C...
    ..BB.................C...
    ..BB.................C...
    .........................
    
    cost: 184 time: 00:00:28
    .........................
    ......AAAAAAAAAAAAA......
    .........................
    .....B........CCCCCCC....
    .....B........CCCCCCC....
    .....B......D.CCCCCCC....
    .....B......D.CCCCCCC....
    .....B......D.CCCCCCC....
    .....B......D.CCCCCCC....
    .....B......D............
    ..EEEEEE....D............
    ..EEEEEE....D............
    ..EEEEEE....D............
    ..EEEEEE....D............
    ..EEEEEE.................
    ..FFFFFFFFFFFFFFFFFFFFFFF
    
    cost: 186 time: 00:00:03
    ........................................
    ........................................
    ...AAAAAA...............................
    ...AAAAAA...............................
    ...AAAAAA...............................
    ...AAAAAA.........BBBBBBBBBB............
    ...AAAAAA.........BBBBBBBBBB............
    ..................BBBBBBBBBB............
    ..................BBBBBBBBBB............
    .............CCCCCCCCCCCCCCC............
    .............CCCCCCCCCCCCCCC............
    ........DDDDDDDDDDDD....................
    ........DDDDDDDDDDDD....................
    ........EEEEEE..........................
    ........EEEEEE..........................
    ........................................
    ........................................
    ........................................
    
    cost: 185 time: 00:01:24
    ........................................
    ..AA.B.CCC..............................
    ..AA.B.CCC............DDDD..............
    ..AA.B.CCC............DDDD..............
    ..AA.B.CCC..............................
    ..AA.B.CCC..............EEEE............
    ..AA.B..................EEEE............
    ..AA.B..................................
    ..AA.B..................................
    ..AA.B..............FFFFFFFF............
    ..AA.B..............FFFFFFFF............
    ..AA.B..............FFFFFFFF............
    ..AA.B..............FFFFFFFF............
    ..AA.B..................................
    ..AA.B................GGGG..............
    ..AA.B..................................
    ..AA.B..................................
    ........................................
    
    cost: 196 time: 00:00:03
    AAAAA...................................
    AAAAA...................................
    AAAAA...................................
    AAAAA...................................
    AAAAA...................................
    AAAAA...........BBBBBBBBBBB.............
    AAAAA...........BBBBBBBBBBB.............
    ....................CCCC................
    ....................CCCC................
    ....................CCCC................
    ....................CCCC................
    ....................CCCC................
    ...............DEEEEEEEEEEEEE...........
    ...............DEEEEEEEEEEEEE...........
    .......FFFFFFFFDEEEEEEEEEEEEE...........
    .......FFFFFFFFD........................
    ........................................
    ........................................
    ........................................
    
    cost: 368 time: 00:03:45
    ...............AAAAAAAAA................
    ...............AAAAAAAAA................
    ..........BBBBBBBBBBBBBBBBBBB...........
    ..........BBBBBBBBBBBBBBBBBBB...........
    ..........BBBBBBBBBBBBBBBBBBB...........
    .......CCC...................DDD........
    .......CCC...................DDD........
    .......CCC....EEEEEEEEEEEE...DDD........
    .......CCC....EEEEEEEEEEEE...DDD........
    .......CCC...................DDD........
    .......CCC...................DDD........
    .......CCC.........FF........DDD........
    .......CCC.........FF........DDD........
    .......CCC...................DDD........
    .......CCC...................DDD........
    .......CCC.....GGGGGGGGG.....DDD........
    .......CCC.....GGGGGGGGG.....DDD........
    .........HHH...............III..........
    .........HHH...............III..........
    .........HHH...............III..........
    .........HHH...............III..........
    .........HHH...............III..........
    ............JJJJJJJJJJJJJJJ.............
    ............JJJJJJJJJJJJJJJ.............
    ............JJJJJJJJJJJJJJJ.............
    
    9 field(s). Total cost is $1486
    Total time is 00:05:48

    > python2.6 s2.py rectangles.txt
    cost: 41 time: 00:00:00
    .............
    .............
    .............
    ...AAAA......
    ...AAAA......
    ...AAAA......
    .......BBB...
    .......BBB...
    .......BBB...
    .............
    
    cost: 62 time: 00:00:00
    .............
    ..AAAAAA.....
    ..AAAAAA.....
    ..AAAAAA.....
    ..AAAAAA.....
    ..AAAAAA.....
    ..AAAAAA.....
    ..........BBB
    ..........BBB
    
    cost: 71 time: 00:00:00
    .........A...
    .........A...
    BBBBBBBBBA...
    ..C......A...
    ..C......A...
    ..C......A...
    ..CDDDDDDDDDD
    ..C..........
    ..C..........
    
    cost: 181 time: 00:00:03
    .........................
    ..AAAAAAAAAAAAAAAAAAAA...
    ..AAAAAAAAAAAAAAAAAAAA...
    ..BB.................C...
    ..BB.................C...
    ..BB.......DDD.......C.E.
    ..BB.......DDD.......C...
    ..BB...FFFFDDDGGGGGGGC...
    ..BB...FFFFDDDGGGGGGGC...
    ..BB.......DDD.......C...
    ..BB.......DDD.......C...
    ..BB.................C...
    ..BB.................C...
    .........................
    
    cost: 184 time: 00:06:04
    .........................
    ......AAAAAAAAAAAAA......
    .........................
    .....B........CCCCCCC....
    .....B........CCCCCCC....
    .....B......D.CCCCCCC....
    .....B......D.CCCCCCC....
    .....B......D.CCCCCCC....
    .....B......D.CCCCCCC....
    .....B......D............
    ..EEEEEE....D............
    ..EEEEEE....D............
    ..EEEEEE....D............
    ..EEEEEE....D............
    ..EEEEEE.................
    ..FFFFFFFFFFFFFFFFFFFFFFF
    
    cost: 186 time: 00:00:17
    ........................................
    ........................................
    ...AAAAAA...............................
    ...AAAAAA...............................
    ...AAAAAA...............................
    ...AAAAAA.........BBBBBBBBBB............
    ...AAAAAA.........BBBBBBBBBB............
    ..................BBBBBBBBBB............
    ..................BBBBBBBBBB............
    .............CCCCCBBBBBBBBBB............
    .............CCCCCBBBBBBBBBB............
    ........DDDDDDDDDDDD....................
    ........DDDDDDDDDDDD....................
    ........EEEEEE..........................
    ........EEEEEE..........................
    ........................................
    ........................................
    ........................................
    
    cost: 185 time: 00:02:32
    ........................................
    ..AA.B.CCC..............................
    ..AA.B.CCC............DDDD..............
    ..AA.B.CCC............DDDD..............
    ..AA.B.CCC..............................
    ..AA.B.CCC..............EEEE............
    ..AA.B..................EEEE............
    ..AA.B..................................
    ..AA.B..................................
    ..AA.B..............FFFFFFFF............
    ..AA.B..............FFFFFFFF............
    ..AA.B..............FFFFFFFF............
    ..AA.B..............FFFFFFFF............
    ..AA.B..................................
    ..AA.B................GGGG..............
    ..AA.B..................................
    ..AA.B..................................
    ........................................
    
    cost: 196 time: 00:00:27
    AAAAA...................................
    AAAAA...................................
    AAAAA...................................
    AAAAA...................................
    AAAAA...................................
    AAAAA...........BBBBBBBBBBB.............
    AAAAA...........BBBBBBBBBBB.............
    ....................CCCC................
    ....................CCCC................
    ....................CCCC................
    ....................CCCC................
    ....................CCCC................
    ...............DEEEEEEEEEEEEE...........
    ...............DEEEEEEEEEEEEE...........
    .......FFFFFFFFDEEEEEEEEEEEEE...........
    .......FFFFFFFFD........................
    ........................................
    ........................................
    ........................................
    
    cost: 368 time: 06:40:23
    ...............AAAAAAAAA................
    ...............AAAAAAAAA................
    ..........BBBBBBBBBBBBBBBBBBB...........
    ..........BBBBBBBBBBBBBBBBBBB...........
    ..........BBBBBBBBBBBBBBBBBBB...........
    .......CCC...................DDD........
    .......CCC...................DDD........
    .......CCC....EEEEEEEEEEEE...DDD........
    .......CCC....EEEEEEEEEEEE...DDD........
    .......CCC...................DDD........
    .......CCC...................DDD........
    .......CCC.........FF........DDD........
    .......CCC.........FF........DDD........
    .......CCC...................DDD........
    .......CCC...................DDD........
    .......CCC.....GGGGGGGGG.....DDD........
    .......CCC.....GGGGGGGGG.....DDD........
    .........HHH...............III..........
    .........HHH...............III..........
    .........HHH...............III..........
    .........HHH...............III..........
    .........HHH...............III..........
    ............JJJJJJJJJJJJJJJ.............
    ............JJJJJJJJJJJJJJJ.............
    ............JJJJJJJJJJJJJJJ.............
    
    9 field(s). Total cost is $1474
    Total time is 06:49:50
