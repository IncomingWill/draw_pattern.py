# Title: Draw Pattern Program
# Program created by William Schaeffer
# CPS 313
# P. 216, Exercise 14, Draw Pattern Program
# 01.25.22

# This program will use nested loops to draw a sweet star pattern

STAR = '*'                      #constant star variable
baseSize = 7

for r in range(baseSize):
    for c in range(baseSize - r):
        print(STAR, end='')
    print()