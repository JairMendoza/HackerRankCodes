#!/bin/python3

import math
import os
import random
import re
import sys

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    board = [0] * n
    mov = 0
    for i in range(n):
        board[i] = [0] * n
    #if k > 0:
        #poner los obstaculos en el tablero
    #poner la reina 
    board[r_q-1][c_q-1] = 'R'
    
    mov += len(board) - r_q  #moviminetos arriba
    mov += r_q -1          #movimientos abajo
    mov += len(board) - c_q #movimientos lado derecho
    mov += c_q -1          #movimientos lado izquierdo     
    if len(board) - r_q or len(board) - c_q != 0:
        if len(board) - r_q < len(board) - c_q:
            mov += len(board) - r_q#moviminetos ezquina superior derecha
        else:
            mov += len(board) - c_q 
    if len(board) - r_q  or c_q -1 != 0:
        if len(board) - r_q  < c_q -1:
            mov += len(board) - r_q #moviminetos ezquina superior izquierda
        else:
            mov += c_q -1
    if r_q -1 or c_q -1 != 0:
        if r_q -1 < c_q -1:
            mov += r_q -1 #movimientos ezquina inferior izquierda
        else:
            mov += c_q -1
    if r_q -1 or len(board) - c_q != 0:
        if r_q -1 < len(board) - c_q:
            mov += r_q -1#movimientos ezquina inferior derecha
        else:
            mov += len(board) - c_q
    return mov
    
         

if __name__ == '__main__':
    

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)
