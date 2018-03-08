import random #used for generation of numbers
import threading # used to make a threading
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

#import random
#import numpy as np
#import matplotlib.pyplot as plt


import sys #import Tkinter
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
    from tkinter import messagebox

root = Tk.Tk() #create object
root.wm_title("Random walk") #title
menu = Tk.Menu(root) # create Menu
root.config(menu=menu)

def openFrame(): #create About window
    AboutFrame = Tk.Toplevel()
    AboutFrame.geometry("400x300")
    AboutFrame.title("About")
    T = Tk.Text(AboutFrame, )
    T.pack()

    info =  """
A simple program for 2D random walk.

Developed by Mieni
"""
    T.insert(Tk.END, info)
    T['state']='disabled' # disable the editing

helpmenu = Tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...",command=openFrame)

#create frames and their geometry( I used more columns than necessary)
toolframe=Tk.Frame(root)
toolframe.grid(row=0,columnspan=4,sticky=Tk.W)
upframe=Tk.Frame(root)
upframe.grid(row=1,columnspan=4)
buttonframe=Tk.Frame(root)
buttonframe.grid(row=2,columnspan=4)

#create the plot figure
figure_plot = Figure()
plot = figure_plot.add_subplot(111)
plot.grid()
plot.set_title("Random walk")

canvas = FigureCanvasTkAgg(figure_plot, master=upframe)
canvas.show()
canvas.get_tk_widget().grid(columnspan=4)

toolbar = NavigationToolbar2TkAgg(canvas, toolframe)
toolbar.update()
canvas._tkcanvas.grid(columnspan=4)

#create a diferent thred in order for the program not to halt while generating random numbers
def call_plot():
    thred=threading.Thread(target=_cal)
    thred.start()
#draw the plot
def _cal():
    plot.clear()
    steps=int(entry_field.get()) #get the max_iteration from entry field

#see how many dots are going to be generated to see wether to draw the first 10, where the deviation from Pi is segnificant
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

    plot.set_title("Random walk")
    plot.plot(pos[:,0],pos[:,1])
    plot.grid()
    canvas.draw()

#button for the plotting
Plot_btn = Tk.Button(master=buttonframe, text='Plot', command=call_plot)
Plot_btn.grid(row=1,column=5)

#entry field to get the max # of generated numbers
Tk.Label(buttonframe,text='Max # of generated numbers').grid(row=1,column=0,)
entry_field=Tk.Entry(buttonframe,width=7)
entry_field.insert(0,"1000")
entry_field.grid(row=1,column=1,sticky=Tk.W)

Tk.mainloop()
