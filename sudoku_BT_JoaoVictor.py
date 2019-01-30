import pandas as pd
import numpy as np
from math import log,floor

def read_ent():
	arq = open('ent_sudoku.txt', 'r')
	texto = arq.readlines()
	return texto

def test_number( matriz, num, i, j): #verfifica se o numero é valido na posição: horizontal, vertical e matriz3x3
	#print("is valid ", i,j,num)
	verify_row = all([num != int(matriz[i][j]) for j in range(9)]) # verifica horizontalmente
	#print('linha:', verify_row)
	if verify_row == True:
		verify_coll = all([num != int(matriz[i][j]) for i in range(9)]) # verifica verticalmente
		#print('Coluna:', verify_coll)
		if verify_coll == True:
			#print('antes',i,j)
			i = (floor(i/3)) * 3
			j = (floor(j/3)) * 3
			#print('depois',i,j)
			for x in range(i, i+3): # Verifica a matriz 3x3
				for y in range(j, j+3):
					#print(int(matriz[x][y]))
					if int(matriz[x][y]) == num:
						return False
		else:
			return False
	else:
		return False

	return True

def findNextEmptyCell(matriz, i, j):
	for i in range(i,9):
		for j in range(j,9):
			if int(matriz[i][j]) == 0:
				return i,j

	for i in range(0,9):
		for j in range(0,9):
			if matriz[i][j] == 0:
				return i,j
	return -1, -1

def solve_sudoku( matriz, i=0, j=0):
	i,j = findNextEmptyCell(matriz, i, j)
	
	if(i == -1):
		print('\nY \n', end='')
		for m in range(9):
			for n in range(9):
				print(int(matriz[m][n]), end='')
		return True

	for k in range (1,10):
		if test_number(matriz, k, i, j) == True:
			matriz[i][j] = k
			if solve_sudoku(matriz, i, j):
				return True

			matriz[i][j] = 0

	return False

def read_sudoku(entrada):
	matriz = [[0]*9 for i in range(9)]
	#matriz_inicial = [[0]*9 for i in range(9)]
	k=0
	for i in range(9):
		for j in range(9):
			if entrada[k] != '.':
				matriz[i][j] = entrada[k]
				
			k+=1
	return matriz

def main():
	entrada = read_ent()

	for i in range(int(entrada[0])):
		matriz = read_sudoku(entrada[i+1])
		sudoku_resolvido = solve_sudoku(matriz)
		if(sudoku_resolvido == False):
			print('N\n')
		print('\n')
main()