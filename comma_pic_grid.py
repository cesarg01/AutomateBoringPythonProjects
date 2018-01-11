# Chapter 4 Practice Projects from Automate the Boring Stuff With Python.
def comma(list):
    """
    # Take a list of values and returns a string with all the items separated by a comma and a space, with and inserted
    # before the last item.
    """
    words = ''
    for i in range(len(list)):
        if i == len(list) - 1:
            words = words + 'and ' + list[i]
        else:
            words = words + list[i] + ', '
    return words


def printer(grid):
    """
    # Take a grid and printed a certain way.
    """
    cols = len(grid[0]) # The number of columns
    rows = len(grid) # The number of rows

    for i in range(cols):
        for j in range(rows):
            print(grid[j][i], end='')
        print()

spam = ['apples', 'bananas', 'tofu', 'cats', 'berry']
print(comma(spam))

grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.'],
]

printer(grid)