"""
In a game, a frog is located in a 10x6 grid. The frog position is marked by a character "F" and other positions are
marked by a character "x"

Write a program to ask user to enter the frog position and then display the game grid. Study the following examples
carefully and write a program that works exactly like the examples. The program does not need to handle user input
error.

For example:
Input	                    Result
2                           Please enter row: 2
a                           Please enter column: a
                            Here is the game grid:
                                1 2 3 a b c
                            a | x x x x x x |
                            b | x x x x x x |
                            c | x x x x x x |
                            d | x x x x x x |
                            e | x x x x x x |
                            1 | x x x x x x |
                            2 | x x x F x x |
                            3 | x x x x x x |
                            4 | x x x x x x |
                            5 | x x x x x x |
d                           Please enter row: d
2                           Please enter column: 2
                            Here is the game grid:
                                1 2 3 a b c
                            a | x x x x x x |
                            b | x x x x x x |
                            c | x x x x x x |
                            d | x F x x x x |
                            e | x x x x x x |
                            1 | x x x x x x |
                            2 | x x x x x x |
                            3 | x x x x x x |
                            4 | x x x x x x |
                            5 | x x x x x x |
"""
rows = input("Please enter row: ")
columns = input("Please enter column: ")

grid = {'a1': 'x', 'a2': 'x', 'a3': 'x', 'aa': 'x', 'ab': 'x', 'ac': 'x',
              'b1': 'x', 'b2': 'x', 'b3': 'x', 'ba': 'x', 'bb': 'x', 'bc': 'x',
              'c1': 'x', 'c2': 'x', 'c3': 'x', 'ca': 'x', 'cb': 'x', 'cc': 'x',
              'd1': 'x', 'd2': 'x', 'd3': 'x', 'da': 'x', 'db': 'x', 'dc': 'x',
              'e1': 'x', 'e2': 'x', 'e3': 'x', 'ea': 'x', 'eb': 'x', 'ec': 'x',
              '11': 'x', '12': 'x', '13': 'x', '1a': 'x', '1b': 'x', '1c': 'x',
              '21': 'x', '22': 'x', '23': 'x', '2a': 'x', '2b': 'x', '2c': 'x',
              '31': 'x', '32': 'x', '33': 'x', '3a': 'x', '3b': 'x', '3c': 'x',
              '41': 'x', '42': 'x', '43': 'x', '4a': 'x', '4b': 'x', '4c': 'x',
              '51': 'x', '52': 'x', '53': 'x', '5a': 'x', '5b': 'x', '5c': 'x'}


concat = str(rows) + str(columns)
grid[concat] = 'F'


print("Here is the game grid:")
print("    1 2 3 a b c")
print("a | {0} {1} {2} {3} {4} {5} |".format(grid['a1'], grid['a2'], grid['a3'], grid['aa'], grid['ab'], grid['ac']))
print("b | {0} {1} {2} {3} {4} {5} |".format(grid['b1'], grid['b2'], grid['b3'], grid['ba'], grid['bb'], grid['bc']))
print("c | {0} {1} {2} {3} {4} {5} |".format(grid['c1'], grid['c2'], grid['c3'], grid['ca'], grid['cb'], grid['cc']))
print("d | {0} {1} {2} {3} {4} {5} |".format(grid['d1'], grid['d2'], grid['d3'], grid['da'], grid['db'], grid['dc']))
print("e | {0} {1} {2} {3} {4} {5} |".format(grid['e1'], grid['e2'], grid['e3'], grid['ea'], grid['eb'], grid['ec']))
print("1 | {0} {1} {2} {3} {4} {5} |".format(grid['11'], grid['12'], grid['13'], grid['1a'], grid['1b'], grid['1c']))
print("2 | {0} {1} {2} {3} {4} {5} |".format(grid['21'], grid['22'], grid['23'], grid['2a'], grid['2b'], grid['2c']))
print("3 | {0} {1} {2} {3} {4} {5} |".format(grid['31'], grid['32'], grid['33'], grid['3a'], grid['3b'], grid['3c']))
print("4 | {0} {1} {2} {3} {4} {5} |".format(grid['41'], grid['42'], grid['43'], grid['4a'], grid['4b'], grid['4c']))
print("5 | {0} {1} {2} {3} {4} {5} |".format(grid['51'], grid['52'], grid['53'], grid['5a'], grid['5b'], grid['5c']))



