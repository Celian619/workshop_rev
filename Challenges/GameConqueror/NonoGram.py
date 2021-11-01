#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 20:44:04 2020

@author: celian
"""
import tkinter as Tk 
import random


nb_puzzle_reussi = 0

nb_hints = 63637483

size = 15
pas=600 / size 
fenetre = Tk.Tk() 
canvas = Tk.Canvas(fenetre,height=800,width=800) 
listIDrectangles = [[0]* size for i in range(size)]

def randomPlayground(size):
    matrix = [[0]* size for i in range(size)]
    
    for i in range(160):
        x = random.randint(0,14)
        y = random.randint(0,14)
        matrix[x][y] = 1
    
    return matrix

playground = randomPlayground(size)

for i in range(size) :
    textBlocks = ""
    
    suite = 0
    for j in range(size) :
        if playground[i][j] == 1 :
            suite += 1
        elif suite > 0:
            textBlocks +=  "\n" + str(suite)
            suite = 0
    
    
    
    if suite > 0:
            textBlocks +=  "\n" + str(suite)
            suite = 0
    
    canvas.create_text(pas*i+120, 70, text=textBlocks)
    
    textBlocks = ""
    for j in range(size) :
        if playground[j][i] == 1 :
            suite += 1
        elif suite > 0:
            textBlocks +=  " " + str(suite)
            suite = 0
    if suite > 0:
            textBlocks +=  " " + str(suite)
    canvas.create_text(40,pas*i+165,text=textBlocks)


    
for i in range(size): 
    for j in range(size): 
        listIDrectangles[i][j] = canvas.create_rectangle(pas*i+100, pas*j+140, pas*(i+1)+100, pas*(j+1)+140, fill='#666666') 
                        
# lignes comme sudoku
for a in [1,2] :
         canvas.create_line(100, pas*5*a+142, 700, pas*5*a+142, width = 4)
         canvas.create_line(pas*5*a+102, 140, pas*5*a+102, 740, width = 4)             

 
canvas.pack()


def remplie(x,y):
    canvas.itemconfig(listIDrectangles[x][y],fill='#333333')
    fenetre.update()
    
def vider(x,y):
    canvas.itemconfig(listIDrectangles[x][y],fill='#888888')
    fenetre.update()  
    
def vert(x,y):
    canvas.itemconfig(listIDrectangles[x][y],fill='#EEEEEE')
    fenetre.update()

def click(test):
    
    mouseX = test.x
    mouseY = test.y
    blockX = int((mouseX-100)//pas)
    blockY = int((mouseY-142)//pas)
    if size > blockX and blockX >= 0 and size > blockY and blockY >= 0 :
        if test.state == 16:#click compose
            if test.num == 1:
                vert(blockX,blockY)
            elif test.num == 3:
                remplie(blockX,blockY)
        else :
            vider(blockX,blockY)

def aide():
	global nb_hints
	if nb_hints>0:
		nb_hints-=1
		button.config(text="hint ("+str(nb_hints)+")")
		for i in range(10):
			x = random.randint(0,14)
			y = random.randint(0,14)
			if playground[x][y] == 1:
				remplie(x,y)
			else:
				vert(x,y)
      

canvas.bind("<Button 1>", click)
canvas.bind("<Button 3>", click)

button = Tk.Button(text = "hint ("+str(nb_hints)+")", command= aide)
button.pack()

"""
button2 = Tk.Button(text = 'vert', command= vert)
button2.pack()
"""
fenetre.mainloop()
