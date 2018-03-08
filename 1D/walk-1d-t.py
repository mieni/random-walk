import random
import numpy as np
import matplotlib.pyplot as plt




def draw(steps,lines):

    for i in range(1,lines):
        x=[]
        x.append(0)#position in the begining
        for num in range(1,steps):
            prob =random.random()#random number

            if prob < 0.5:
                x.append(x[num-1]+1)#step up
            else:
                x.append(x[num-1]-1)#step down

        plt.plot(x) #add line
    #format plot
    plt.title("Random walk")
    plt.axhline(0)
    plt.xlabel('Time')
    plt.ylabel('x')
    plt.grid()
    plt.show()


#a simple menu for the program
info =  """
A simple program for multiple 1D random walks.

Developed by Mieni

"""
print(info)
#main loop
while 1:
    inp = input("Enter <exit> to exit \nPlease enter steps, lines: ")
    print('\n')
    if inp == 'exit':
        break #exit if exit
    else:
        try:
            steps,lines = inp.split()#get the number of steps and lines
            steps=int(steps)
            lines=int(lines)
            draw(steps,lines) #plot
        except ValueError:
            #Handle the exception
            print ('\nPlease enter an integer values for steps, lines\n')
