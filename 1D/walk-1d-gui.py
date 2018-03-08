import random #used for generation of numbers
import threading # used to make a threading
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


import sys #import Tkinter
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
    from tkinter import messagebox

root = Tk.Tk() #create object
root.wm_title("1D Random walk") #title
menu = Tk.Menu(root) # create Menu
root.config(menu=menu)

def openFrame(): #create About window
    AboutFrame = Tk.Toplevel()
    AboutFrame.geometry("400x300")
    AboutFrame.title("About")
    T = Tk.Text(AboutFrame, )
    T.pack()

    info =  """
A simple program for multiple 1D random walks..

Developed by Mieni
"""
    T.insert(Tk.END, info)
    T['state']='disabled' # disable the editing

helpmenu = Tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...",command=openFrame)

#create frames and their geometry
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
plot.set_xlabel("Steps")
plot.set_ylabel("X")

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
    steps=int(steps_field.get()) #get the max_iteration from entry field
    lines=int(lines_field.get()) #get the max_iteration from entry field
    for i in range(0,lines):
        x=[]
        x.append(0)#position in the begining
        for num in range(1,steps):
            prob =random.random()#random number

            if prob < 0.5:
                x.append(x[num-1]+1)#step up
            else:
                x.append(x[num-1]-1)#step down

        plot.plot(x) #add line
    #format plot
    plot.set_title("Random walk")
    plot.set_xlabel("Steps")
    plot.set_ylabel("X")
    plot.axhline(0)
    plot.grid()
    canvas.show()



#button for the plotting
Plot_btn = Tk.Button(master=buttonframe, text='Plot', command=call_plot)
Plot_btn.grid(row=1,column=5)

#entry field to get the # of steps
Tk.Label(buttonframe,text='Steps').grid(row=1,column=0,)
steps_field=Tk.Entry(buttonframe,width=7)
steps_field.insert(0,"1000")
steps_field.grid(row=1,column=1,sticky=Tk.W)

#entry field to get the # of lines
Tk.Label(buttonframe,text='Lines').grid(row=1,column=2,)
lines_field=Tk.Entry(buttonframe,width=7)
lines_field.insert(0,"5")
lines_field.grid(row=1,column=3,sticky=Tk.W)

Tk.mainloop()
