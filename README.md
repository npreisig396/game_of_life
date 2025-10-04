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
