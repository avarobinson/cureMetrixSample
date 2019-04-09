"""
CureMetrix Python Interview Questions
Ava Robinson

"""

"""---------------------------------MATH QUESTIONS-----------------------------------"""


"""
1. Write a function that takes two integers(x and y) and
returns a list of numbers between x and y that are divisible by 5 but not by 7
"""
def divisible(x, y):
    """
    :param x: integer
    :param y: integer
    :return: list of integers between x and y divisible by 5 but not by 7
    """
    divisibleNums = []
    for num in range(x+1,y):
        if num % 5 == 0 and num % 7 != 0:
            divisibleNums.append(num)
    return divisibleNums


"""

2. Write a function that takes two numbers (x and y) as input and 
returns the value to the following function:
f(x) = x*y, if x>=0, y>=0
f(x) = 0, otherwise

"""
def function(x,y):
    """
    :param x: number
    :param y: number
    :return: result of function f(x)
    """
    if x >= 0 and y >= 0:
        return x*y
    else:
        return 0


""" -------------------------------------------GAMES---------------------------------------- """



"""
1. You have a chessboard with only the Rook on it. The Rook can move up, down, left or right from your perspective. 
Write a function (or a class) that takes a series of movements and at the end of the sequence of movements prints 
two numbers:
    a. The distance traveled by the Rook
    b. How far away the Rook is from its starting point
"""
def chessboard(movements):
    """
    :param movements: a list of list of movements with each inner list containing the direction and the number of spaces moved
    :return: the distance traveled by the Rook and how far away the Rook is from starting point
    """
    x = 0
    y = 0
    distance = 0
    for move in movements:
        direction = move[0]
        amount = move[1]
        distance += amount
        if direction == "up":
            y += amount
        elif direction == "down":
            y -= amount
        elif direction == "right":
            x += amount
        elif direction == "left":
            x -= amount

    fromStart = abs(x) + abs(y)

    return "Total distance traveled: " + str(distance) + "\nSpaces away from start: " + str(fromStart)
