# 
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

cols = len(grid[0])
rows = len(grid)

for i in range(cols):
    for j in range(rows):
        print(grid[j][i], end='')
    print()