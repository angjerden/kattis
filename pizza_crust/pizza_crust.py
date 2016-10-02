'''
George has bought a pizza. George loves cheese.
George thinks the pizza does not have enough cheese.
George gets angry.

George’s pizza is round,
and has a radius of R cm. The outermost C cm is crust,
and does not have cheese. What percent of George’s pizza has cheese?

Input

Each test case consists of a single line
with two space separated integers, R and C

.
Output

For each test case, output the percentage
of the pizza that has cheese.
Your answer must have an absolute or relative error of at most 10^6.
.

Limits

    1≤C≤R≤100
'''

from sys import stdin
import math

line = stdin.readline()
line = line.split(' ')
r = int(line[0])
c = int(line[1])
r_cheese = r - c

area = math.pi * math.pow(r, 2)
area_cheese = math.pi * math.pow(r_cheese, 2)

percent_not_cheese = (area_cheese / area) * 100
print(percent_not_cheese)
