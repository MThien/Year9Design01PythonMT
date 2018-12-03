import tkinter as tk

def submit():
	print("Submit Pressed")
	list.append(slide1.get())
	list.append(slide2.get())
	list.append(slide3.get())
	print(list)

def change(*args):
	print("Button Changed")
list = []

root = tk.Tk()
root.title("Bowel Movement Tracker")

#------------------- LABELS -------------------

label = tk.Label(root, text = "Bowel Movements Per Week")
label.grid(row = 0, column = 0, columnspan = 2)

label = tk.Label(root, text = "Water Drank Per Week (mL)")
label.grid(row = 3, column = 0, columnspan = 2)

label = tk.Label(root, text = "Food Eaten")
label.grid(row = 6, column = 0, columnspan = 1)

#-------------------- ENT --------------------

slide1 = tk.Scale(root, from_=0, to=30, resolution= 1, orient=tk.HORIZONTAL)
slide1.grid(row = 1, column = 0, columnspan = 1)

slide2 = tk.Scale(root, from_=0, to=30, resolution= 1, orient=tk.HORIZONTAL)
slide2.grid(row = 4, column = 0, columnspan = 1)

#slide3 = tk.Scale(root, from_=0, to=30, resolution= 1, orient=tk.HORIZONTAL)
#slide3.grid(row = 7, column = 0, columnspan = 1)

#-------------------- Buttons ------------------

btn = tk.Button(root, text = "Submit", command = submit)
btn.grid (row = 1, column = 2)

#-------------------- Drop Down List ------------------
#Step 1: Create a list of everythign that is in the drop 
DROPDOWNLIST = ["Option 1","Option 2","Option 3"]
#Step 2: Create a variable to trace/track the current option selelcted
ddvar = tk.StringVar(root)
#Step 3: Set the inital value of ddvar (what is your drop down initalized to)
ddvar.set(DROPDOWNLIST[0])
#Step 3A: Attach a function that runs when I change ddvar
ddvar.trace("w",change)
#Step 4: Create the drow down menu
omenu = tk.OptionMenu(root, ddvar, DROPDOWNLIST[0], DROPDOWNLIST[1],DROPDOWNLIST[2])
#Step 5: Pack it in the window
omenu.grid(row = 7, column = 0)






































root.mainloop()