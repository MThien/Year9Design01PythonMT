import tkinter as tk


root = tk.Tk()
root.title("Bowel Movement Tracker")
root.configure(background="mediumslateblue")


def submit():
	print("Submit Pressed")
	list.append(slide1.get())
	list.append(slide2.get())
	list.append(slide3.get())
	list.append(ent1.get())
	list.append(ent2.get())

def record():
	print("Record Pressed")
	list.append(ent1.get())
	list.append(ent2.get())
	textbox0.insert('1.0', ent1.get() + ", " + ent2.get() + "\n")
	ent1.delete(0, tk.END)
	ent2.delete(0, tk.END)
	#for x in range(len(list)): 
    	#print (str(list[x]))
    	#textbox0.insert(list[x])

def change(*args):
	print("Button Changed")
list = []
#------------------- LABELS -------------------
label00 = tk.Label(root, text = "", background = "darkslateblue")
label00.grid(row = 0, column = 0, sticky = "NESW")

label0 = tk.Label(root, text = "Bowel Movement Tracker", background = "darkslateblue", foreground = "white", height = 2)
label0.grid(row = 0, column = 1, sticky = "NESW")

label1 = tk.Label(root, text = "Bowel Movements Per Week", background = "darkslateblue", foreground = "white", height = 2)
label1.grid(row = 1, column = 0, sticky = "NESW")

label2 = tk.Label(root, text = "Water Drank Per Week (L)", background = "darkslateblue", foreground = "white", height = 2)
label2.grid(row = 3, column = 0, sticky = "NESW")

label3 = tk.Label(root, text = "Weight (pounds)", background = "darkslateblue", foreground = "white", height = 2)
label3.grid(row = 5, column = 0, sticky = "NESW")

label4 = tk.Label(root, text = "Type of Food Eaten", background = "darkslateblue", foreground = "white", height = 2)
label4.grid(row = 7, column = 0, sticky = "NESW")

label5 = tk.Label(root, text = "Amount of Fibers in food (grams)", background = "darkslateblue", foreground = "white", height = 2)
label5.grid (row = 9, column = 0, sticky = "NESW")

label6 = tk.Label(root, text = "", background = "darkslateblue")
label6.grid(row = 10, column = 0, sticky = "NESW")

labelfiller = tk.Label(root, text = "", background = "darkslateblue")
labelfiller.grid(row = 11, column = 0, sticky = "NESW")

labelfiller2 = tk.Label(root, text = "", background = "darkslateblue")
labelfiller2.grid(row = 0, column = 2, sticky = "NESW")

#-------------------- ENT --------------------

slide1 = tk.Scale(root, from_=0, to=50, resolution= 1, length = 300, tickinterval= 10, orient=tk.HORIZONTAL)
slide1.grid(row = 1, column = 1)
slide1.configure(background="mediumslateblue", foreground = "white")

slide2 = tk.Scale(root, from_=0, to=30, resolution= 1, length = 300,  tickinterval= 10, orient=tk.HORIZONTAL)
slide2.grid(row = 3, column = 1)
slide2.configure(background="mediumslateblue", foreground = "white")

slide3 = tk.Scale(root, from_=0, to=300, resolution= 1, length = 300, tickinterval= 50, orient=tk.HORIZONTAL)
slide3.grid(row = 5, column = 1)
slide3.configure(background="mediumslateblue", foreground = "white")

#-------------------- Buttons ------------------

btnsubmit = tk.Button(root, text = "Submit", command = submit, height = 2, width = 10)
btnsubmit.grid (row = 10, column = 2)
btnsubmit.configure(background="mediumslateblue")

btnrecord = tk.Button(root, text = "Record", command = record, height = 2, width = 10)
btnrecord.grid (row = 10, column = 1)
btnrecord.configure(background="mediumslateblue")


#-------------------- Food Eaten ---------------

ent1 = tk.Entry(root)
ent1.grid(row = 7, column = 1)
ent1.configure(background="lightgray")

ent2 = tk.Entry(root)
ent2.grid(row = 9, column = 1, columnspan = 1)
ent2.configure(background="lightgray")

#-------------------- Text Box -----------------

textboxRESULT = tk.Text(root, height = 10, width = 40, borderwidth = 3, relief = tk.GROOVE)
textboxRESULT.config(state = "disabled")
textboxRESULT.grid(row = 11, column = 2)

if slide1.get() > 21:
	textboxRESULT.insert(tk.INSERT, "Result: " + str(slide1.get()) + "\n")

textbox0 = tk.Text(root, height = 10, width = 40, borderwidth = 3, relief = tk.GROOVE)
#textbox0.config(state = "disabled")
textbox0.grid(row = 11, column = 1)
#textbox0.insert('1.0', 'insert')
#-------------------Program--------------------













root.mainloop()