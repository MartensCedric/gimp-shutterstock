from tkinter import *
import tkinter as tk
from tkinter import ttk
import subprocess

ss_gui = None
new_search_bool = True

def open_image(path):
	ss_gui.master.quit
	subprocess.Popen("gimp {}".format(path).split(), stdout=subprocess.PIPE).communicate()

class ShutterStockGUI:
	def __init__(self, master):
		self.master = master
		master.title("Shutter Stock Image Search")
		master.geometry("800x800")
		container = ttk.Frame(master)

		string_to_search = StringVar()

		label = tk.Button(master, text="Big Brain Brotherhood Shutterstock Image Search", command=self.search).pack(side="top")

		self.entry = tk.Entry(master, textvariable=string_to_search)
		self.entry.insert(END, 'Click here to search for an image...')
		self.entry.bind("<Button-1>", self.clear_search_bar)
		self.entry.pack(fill=tk.X)
		
		
		string_to_search.trace("w", self.search)

		canvas = tk.Canvas(container)
		scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
		scrollable_frame = ttk.Frame(canvas)

		scrollable_frame.bind(
			"<Configure>",
			lambda e: canvas.configure(
				scrollregion=canvas.bbox("all")
			)
		)
		canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
		canvas.configure(yscrollcommand=scrollbar.set)

		for r in range(50):
			for c in range(4):
				ttk.Button(scrollable_frame, text="memes").grid(row=r, column=c)

		container.pack()
		canvas.pack(side="left", fill="both", expand=True)
		scrollbar.pack(side="right", fill="y")
		tk.Button(master, text="Import to GIMP", command= lambda : open_image("conuhacks.png")).pack(side="top")

	def search(self, *args):
		text_to_search = self.entry.get()
		print(text_to_search)
	
	def clear_search_bar(self, *args):
		global new_search_bool
		if(new_search_bool):
			self.entry.delete(0, END)
			new_search_bool = False
	

root = tk.Tk()
ss_gui = ShutterStockGUI(root)

root.mainloop()
