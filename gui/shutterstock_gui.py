from tkinter import *
import tkinter as tk
from tkinter import ttk

class ShutterStockGUI:
	def __init__(self, master):
		master.title("Shutter Stock Image Search")

		#self.entry = Entry(master)
		#self.entry.grid(row=0, column=1)

		#self.label = Button(master, text="Search")
		#self.label.grid(row=0, column=2)

		master.geometry("800x800")
		container = ttk.Frame(master)
		
		label = tk.Button(master, text="Search", command=self.search).pack(side="top")
		self.entry = tk.Entry(master)
		self.entry.pack(fill=tk.X)

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

	def search(self):
		print(self.entry.get())

root = tk.Tk()
ss_gui = ShutterStockGUI(root)

root.mainloop()
