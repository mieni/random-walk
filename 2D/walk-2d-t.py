import random
import numpy as np
import matplotlib.pyplot as plt




def draw(steps):

    pos = np.zeros((steps,2), dtype='int32')
    t =np.linspace(0, 1, steps)
    t=t
    # print(t)
    for num in range(1,steps):
        prob =random.random()
#        t[num]=num
        if prob < 0.25:
           pos[num][0]=pos[num-1][0]+1
           pos[num][1]=pos[num-1][1]
        elif prob < 0.5:
           pos[num][0]=pos[num-1][0]-1
           pos[num][1]=pos[num-1][1]
        elif prob < 0.75:
           pos[num][1]=pos[num-1][1]+1
           pos[num][0]=pos[num-1][0]
        else:
           pos[num][1]=pos[num-1][1]-1
           pos[num][0]=pos[num-1][0]

    plt.title("Random walk")
    plt.plot(pos[:,0],pos[:,1])
    plt.show()


#draw(20000)
#a simple menu for the program
info =  """
A simple program for 2D random walk.

Developed by Mieni

"""
print(info)
#main loop
while 1:
    inp = input("Enter <exit> to exit \nEnter the number of steps: ")
    print('\n')
    if inp == 'exit':
        break #exit if exit
    else:
        try:
            int(inp) #exception
            draw(int(inp)) #plot
        except ValueError:
            #Handle the exception
            print ('Please enter an integer')
