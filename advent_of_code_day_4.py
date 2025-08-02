"""This word search allows words to be horizontal, vertical, diagonal, written backwards, 
or even overlapping other words. It's a little unusual, though, as you don't merely need 
to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might 
appear, where irrelevant characters have been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....

The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

In this word search, XMAS occurs a total of 18 times; here's the same word search again,
 but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

So I'm searching for all instance of XMAS in a file, but it can come in different directions.
For horizontal it can be left to right or right to left, XMAS or SAMX.
For vertical it can be top to bottom or bottom to top, 
X                          S
M         or               A
A                          M
S                          X
For diagonal it can be four different ways:
X       S S            X
 M     A   A         M
  A   M      M     A
   S X         X S

This gives a total of 8 different ways to find XMAS in the word search. 

The letters can be reused in different instances of XMAS.

An X has to be next to an M, an M has to be next to an A, and an A has to be next to an S.
If an X is not next to an M, it is not part of XMAS.
if an M is not next to an A or next to an X, it is not part of XMAS.
If an A is not next to an S or next to an M, it is not part of XMAS.
These can be replaced with dots. ...

An M could be next to an X and an A, but if that A is not next to an S, that M is not part of XMAS.
The second pass would get rid of that A, and then later that M?

Naive approach:
Run through once for horizontal checks
once for vertical checks
once for diagonal checks
separate input into 2d array so checking is easier?

"""

def read_input(file_path):
    """Read the input file and return a 2D list of characters."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [list(line.strip()) for line in lines if line.strip()]

## helper function to check the surrounding characters
def is_valid_xmas_char(grid, i, j, other_char):
    is_valid = False
    neighbors = [
        (i-1, j), (i+1, j),  # Up, Down 
        (i, j-1), (i, j+1),  # Left, Right
        (i-1, j-1), (i-1, j+1),  # Diagonal Up-Left, Up-Right
        (i+1, j-1), (i+1, j+1)   # Diagonal Down-Left, Down-Right
    ]
    for n in neighbors:
        ni, nj = n
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[ni]):
            if grid[ni][nj] == other_char:
                is_valid = True
                break
    return is_valid

def del_invalid_chars(grid):
    """Replace characters that are not part of XMAS with '.'."""
    d = {
                'X': 'M',
                'M': 'A',
                'A': 'S',
                'S': 'A'
            }
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            
            if not is_valid_xmas_char(grid, i, j, d[grid[i][j]]):
                grid[i][j] = None
    return grid

xmas_grid = read_input('input_day4.txt')

# xmas_grid = del_invalid_chars(xmas_grid)

# horizontal check
def horizontal_check(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i]) - 3):
            if grid[i][j] == 'X' and grid[i][j+1] == 'M' and grid[i][j+2] == 'A' and grid[i][j+3] == 'S':
                count += 1
            elif grid[i][j] == 'S' and grid[i][j+1] == 'A' and grid[i][j+2] == 'M' and grid[i][j+3] == 'X':
                count += 1
    return count

def vertical_check(grid):
    count = 0
    for j in range(len(grid[0])):
        for i in range(len(grid) - 3):
            if grid[i][j] == 'X' and grid[i+1][j] == 'M' and grid[i+2][j] == 'A' and grid[i+3][j] == 'S':
                count += 1
            elif grid[i][j] == 'S' and grid[i+1][j] == 'A' and grid[i+2][j] == 'M' and grid[i+3][j] == 'X':
                count += 1
    return count

def diagonal_check(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    # Top-left to bottom-right
    for i in range(rows - 3):
        for j in range(cols - 3):
            if grid[i][j] == 'X' and grid[i+1][j+1] == 'M' and grid[i+2][j+2] == 'A' and grid[i+3][j+3] == 'S':
                count += 1
            elif grid[i][j] == 'S' and grid[i+1][j+1] == 'A' and grid[i+2][j+2] == 'M' and grid[i+3][j+3] == 'X':
                count += 1

    # Top-right to bottom-left
    for i in range(rows - 3):
        for j in range(3, cols):
            if grid[i][j] == 'X' and grid[i+1][j-1] == 'M' and grid[i+2][j-2] == 'A' and grid[i+3][j-3] == 'S':
                count += 1
            elif grid[i][j] == 'S' and grid[i+1][j-1] == 'A' and grid[i+2][j-2] == 'M' and grid[i+3][j-3] == 'X':
                count += 1

    # Bottom-left to top-right
    for i in range(3, rows):
        for j in range(cols - 3):
            if grid[i][j] == 'X' and grid[i-1][j+1] == 'M' and grid[i-2][j+2] == 'A' and grid[i-3][j+3] == 'S':
                count += 1
            elif grid[i][j] == 'S' and grid[i-1][j+1] == 'A' and grid[i-2][j+2] == 'M' and grid[i-3][j+3] == 'X':
                count += 1

    # Bottom-right to top-left
    for i in range(3, rows):
        for j in range(3, cols):
            if grid[i][j] == 'X' and grid[i-1][j-1] == 'M' and grid[i-2][j-2] == 'A' and grid[i-3][j-3] == 'S':
                count += 1
            elif grid[i][j] == 'S' and grid[i-1][j-1] == 'A' and grid[i-2][j-2] == 'M' and grid[i-3][j-3] == 'X':
                count += 1

    return count/2 # double counted the diagonals accidentally

def diagonal_check_part_2(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    """
    Ways to make the X MAS
    M S
     A
    M S
    I think it's bounded by the number of A's. There's gotta be an A in the center, and the A has to have two M's and two S's
    in the corners, though the orientation is irrelevant.
    """

    poss = [
        "SSMM",
        "MMSS",
        "MSMS",
        "SMSM",
    ]

    # Top-left to bottom-right
    for i in range(1, rows-1):
        for j in range(1, cols-1): # starts at 1 because if an A is on the outer edge it can't make a cross
            if grid[i][j] == 'A':
                s = ""
                corners = [(i+1, j-1),(i+1, j+1),(i-1, j-1),(i-1, j+1)]
                for cx, cy in corners:
                    s += grid[cx][cy]
                if s in poss:
                    count += 1
                    print(s)
            

    return count 


xmas_count = horizontal_check(xmas_grid) + vertical_check(xmas_grid) + diagonal_check(xmas_grid)
mas_count = diagonal_check_part_2(xmas_grid)
print(f"Total instances of XMAS found: {xmas_count}")
print(f"Total instances of MAS found: {mas_count}")