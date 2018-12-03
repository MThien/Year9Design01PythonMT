#This imports the tkinter "tool box" this contains
#all the support material to make GUI elements.
#by including "as tk" we are giving a short name to use.
import tkinter as tk

#Main Window
root = tk.Tk()

#Three stages to build elements/objects
#1. Construct the Object: We build and configure it.
#2. Configure the Object: We specify behaviours and settings
#3. Pack the Object: Put it in the window
output = tk.Text(root,height = 10, width = 30)#Parameters.
output.config(state = "disable", backgroud = "blue")
output.grid(row = 0, column = 0, rowspan= 5)
output.pack()

labInput1 = tk.Label(root, text = "Input 1")
labInput1.pack()

labInput2 = tk.Label(root, text = "Input 2")
labInput2.pack()

labInput3 = tk.Label(root, text = "Input 3")
labInput3.pack()


#What the named parameter variable does is blinds the IntVar to the 
#checkbox. If there is a change in the box, there is a change in the variable.
#This is called BINDING 
c = tk.Checkbutton(root, text="Expand", variable = var)
c.grid(row = 0, column = 1)
cLF = tk.Checkbutton(root, text="Expand", variable = var)
cLF.grid(row = 1, column = 1)
root.mainloop()