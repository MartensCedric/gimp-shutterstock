from tkinter import *

def search():
	print('Now stealing your precious data.')

class MyFirstGUI:
	def __init__(self, master):
		self.master = master
		master.title("Shutter Stock Image Search")

		self.entry = Entry(master)
		self.entry.grid(row=0, column=1)

		self.label = Button(master, text="Search", command=search)
		self.label.grid(row=0, column=2)



root = Tk()
my_gui = MyFirstGUI(root)
root.geometry("600x600")
root.mainloop()
