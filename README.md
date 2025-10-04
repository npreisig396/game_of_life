# Conway's Game of Life with custom of kernels

Board.py opens a pygame window and executes a set of rules based on the kernel file provided

##Usage

`python board.py {path to kernel file}`

##Kernel file format

The kernel files allow you to specify which cells to include in a neighborhood as well as the set of rules which govern the cells living and dying.
The kernel file for Conway's Game of Life is shown below.


3 3

111  
1c1  
111

1:3  
1:4  
0:3

The first line contains two space delimited integers denoting the size of the neighborhood specified in the file. In this case it is a 3x3.
This is followed by an empty line and then the kernel itself, a m by n grid of characters where 0 means the cell is not included, 1 means it is included, and c means it is the cell in question.
The cell itself is always included in the count.

The rules below specify under what circumstances a cell should be alive in the next iteration of the grid. For example, 1:3 means that if a cell is a 1 and its neighborhood count of living cells is 3 then it should be alive in the next iteration. Rather than specify under which conditions a cells die as well, it is assumed that all cells that are not alive according to the rules should be dead in the next iteration.
