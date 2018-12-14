import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Mikey's tabs")
tabControl = ttk.Notebook(root)

root.title("Bowel Movement Tracker")
root.configure(background="mediumslateblue")

#--------------Define Close--------------------
def close_window(): 
    root.destroy()
#--------------Define Record---------------------
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
#--------------Define Reset----------------------
def reset():
	print("Reset Pressed")
	slide1.set("0")
	slide2.set("0")
	slide3.set("0")
	slide4.set("0")
	textboxRESULT.delete('1.0', tk.END)
	textbox0.delete('1.0', tk.END)
#----------------Define Submit--------------------------
def submit():
	print("Submit Pressed")
	list.append(slide1.get())
	list.append(slide2.get())
	list.append(slide3.get())
	list.append(ent1.get())
	list.append(ent2.get())
	list.append(slide4.get())
	
#-----------------If Statements & Else If Statements----------------
	textboxRESULT.insert(tk.INSERT, "The average bowel movements per week is between 3 - 2" + "\n")
	if slide1.get() <= 3:
		textboxRESULT.insert(tk.INSERT, "Your bowel movements per week is WAY BELOW average. It is likely that you are constipated." + "\n")
	elif slide1.get() <= 7 and slide1.get() >= 3:
		textboxRESULT.insert(tk.INSERT, "Your bowel movements per week is lower than average. A possibility is that you may have constipation." + "\n")
	elif slide1.get() >= 17 and slide1.get() <= 21:
		textboxRESULT.insert(tk.INSERT, "Your bowel movements per week is higher than average. A possibility is that you may have diarrhea." + "\n")
	elif slide1.get() >= 21:
		textboxRESULT.insert(tk.INSERT, "Your bowel movements per week is WAY ABOVE average. It is likely that you have diarrhea" + "\n")
	else:
		textboxRESULT.insert(tk.INSERT, "You are in good health (neither constipated or having diarrhea. Keep up the good work.")
	textboxRESULT.insert(tk.INSERT, "\n" + "The average amount of water drank per week can be from one ounce for every pound that you weigh, to 1/2 ounce for every pound you weigh." + "\n")
	if (slide2.get() * 33.814) <= ((slide3.get() / 2) * 7):
		textboxRESULT.insert(tk.INSERT, "The amount of water that you drink per week is below average. If you are constipated, a suggestion can be to drink more water." + "\n")
	if (slide2.get() * 33.814) >= (slide3.get() * 7):
		textboxRESULT.insert(tk.INSERT, "The amount of water that you drink is WAY TOO high. If you have diarrhea, a suggestion would be to decrease amount of water drank." + "\n")
	else:
		textboxRESULT.insert(tk.INSERT,"The amount of water that you drink is healthy. Keep maintaining your water intake." + "\n")
	if slide4.get() <= 2:
		textboxRESULT.insert(tk.INSERT,"Try to aim for eating 19 grams of fibers")
	elif slide4.get() <=8:
		textboxRESULT.insert(tk.INSERT,"Try to aim for eating 25 grams of fibers.")
	elif slide4.get() <= 13:
		textboxRESULT.insert(tk.INSERT,"Try to aim for eating 31 grams of fibers.")
	elif slide4.get() <= 50:
		textboxRESULT.insert(tk.INSERT,"Try to aim for eating 38 grams of fibers.")
	elif slide4.get() > 50:
		textboxRESULT.insert(tk.INSERT,"Try to aim for eating 30 grams of fibers.")
#----------------Defined Change----------------------------
def change(*args):
	print("Button Changed")
list = []
#------------------- Labels -------------------
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

label6 = tk.Label(root, text = "Age", background = "darkslateblue", foreground = "white")
label6.grid(row = 6, column = 0, sticky = "NESW")

labelfiller = tk.Label(root, text = "", background = "darkslateblue")
labelfiller.grid(row = 12, column = 0, sticky = "NESW")

labelfiller0 = tk.Label(root, text = "", background = "darkslateblue")
labelfiller0.grid(row = 11, column = 0, sticky = "NESW")

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

slide4 = tk.Scale(root, from_=0, to=120, resolution = 1, length = 300, tickinterval = 20, orient = tk.HORIZONTAL)
slide4.grid(row = 6, column = 1)
slide4.configure(background="mediumslateblue", foreground = "white")
#-------------------- Buttons ------------------

btnsubmit = tk.Button(root, text = "Submit", command = submit, height = 2, width = 10)
btnsubmit.grid (row = 11, column = 2)
btnsubmit.configure(background="mediumslateblue")

btnrecord = tk.Button(root, text = "Record", command = record, height = 2, width = 10)
btnrecord.grid (row = 11, column = 1)
btnrecord.configure(background="mediumslateblue")

btnclose = tk.Button(root, text = "Close", command = close_window, height = 1, width = 5)
btnclose.grid (row = 0, column = 2, sticky = "E")
btnclose.configure(background = "mediumslateblue")

btnreset = tk.Button(root, text = "Reset", command = reset, height = 1, width = 5)
btnreset.grid(row = 0, column = 2)
#-------------------- Food Eaten ---------------

ent1 = tk.Entry(root)
ent1.grid(row = 7, column = 1)
ent1.configure(background="lightgray")

ent2 = tk.Entry(root)
ent2.grid(row = 9, column = 1, columnspan = 1)
ent2.configure(background="lightgray")

#-------------------- Text Box -----------------

textboxRESULT = tk.Text(root, height = 10, width = 40, borderwidth = 3, relief = tk.GROOVE)
textboxRESULT.grid(row = 12, column = 2)

textbox0 = tk.Text(root, height = 10, width = 40, borderwidth = 3, relief = tk.GROOVE)
#textbox0.config(state = "disabled")
textbox0.grid(row = 12, column = 1)
#textbox0.insert('1.0', 'insert')






root.mainloop()