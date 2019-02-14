#!/usr/bin/env python3
import tkinter

def from7to10(dial):
	try:
		dial = str(float(dial)).split('.')
		dial10 = 0
		for i in range(len(dial[0])):
			dial10 += int(dial[0][-(i + 1)])*(7**i)
			if int(dial[0][-(i + 1)]) >= 7:
				raise UnicodeError
				
		for i in range(len(dial[1])):
			dial10 += int(dial[1][i])*(7**(-(i + 1)))
			if int(dial[1][-(i + 1)]) >= 7:
				raise UnicodeError
		return dial10
	
	except UnicodeError:
		return "This dial isn't in 7th base"
	except ValueError:
		return "Incorrect input"
	
def from10to7(dial):
	try:
		dial = str(float(dial)).split('.')
		aux = int(dial[0])
		dial7 = ''
		while aux != 0:
			dial7 = str(aux % 7) + dial7
			aux = int(aux / 7)
		return dial7
	except ...:
		return "Incorrect input"
	
print(from10to7(input()))
