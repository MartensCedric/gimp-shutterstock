from tkinter import *

class MyFirstGUI:
	def __init__(self, master):
		self.master = master
		master.title("BIG BRAIN TIME")

		self.label = Label(master, text="Test")
		self.label.pack()

		self.greet_button = Button(master, text="Do something", command=self.something)
		self.greet_button.pack()

		self.close_button = Button(master, text="Close", command=master.quit)
		self.close_button.pack()

	def something(self):
		print('something')

root = Tk()
my_gui = MyFirstGUI(root)
root.geometry("400x400")
root.mainloop()
