import tkinter as tk

root = tk.Tk()

labTitle = tk.Label(root,text = "Bowel Movement Tracker", font = ("Helvitica",20))
labTitle.grid(row = 0, column = 0, columnspan = 2)

slide1 = tk.Scale(root, from_= 0, to=30, resolution=0.25, orient=tk.HORIZONTAL)
slide1.grid(row =1, column = 0, columnspan = 2)
slide1.pack()

labtInput1 = tk.Label(root, text = "Bowel Movements Per week")



root.mainloop()