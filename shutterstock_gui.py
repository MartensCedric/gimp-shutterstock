from tkinter import *

class MyFirstGUI:
	def __init__(self, master):
		self.master = master
		master.title("BIG BRAIN TIME")

		self.entry = Entry(master)
		self.entry.grid(row=0, column=1)

		self.label = Button(master, text="Search")
		self.label.grid(row=0, column=2)

	def something(self):
		print('something')

root = Tk()
my_gui = MyFirstGUI(root)
root.geometry("600x600")
root.mainloop()
