from turtle import *



def dragon_curve(order, length, sign=1):
    
    if order == 0:
        forward(length)
    else:
        dragon_curve(order - 1, length, 1)
        right(90 * sign)
        dragon_curve(order - 1, length, -1)