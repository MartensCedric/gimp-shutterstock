from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import subprocess
import time

ss_gui = None
def open_image_gimp(path):
	#ss_gui.master.quit
	subprocess.Popen("gimp {}".format(path).split(), stdout=subprocess.PIPE).communicate()

class SearchResult():
	def __init__(self, path):
		self.path = path

	def open_image(self):
		open_image_gimp(self.path)

class ShutterStockGUI:
	def __init__(self, master):
		self.master = master
		master.title("Shutter Stock Image Search")

		master.geometry("800x800")
		container = ttk.Frame(master)

		string_to_search = StringVar()

		label = tk.Button(master, text="Search", command=self.search).pack(side="top")
		self.entry = tk.Entry(master, textvariable=string_to_search)
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
				image = Image.open('conuhacks.png')
				image = image.resize((100, 100), Image.ANTIALIAS)
				photo = ImageTk.PhotoImage(image)
				label = tk.Label(scrollable_frame, image=photo)
				label.img = photo  # this line is not always needed, but include it anyway to prevent bugs
				label.grid(row=r, column=c)
				search_res = SearchResult("conuhacks.png")
				label.bind("<Button-1>", lambda x : search_res.open_image())

		container.pack()
		canvas.pack(side="left", fill="both", expand=True)
		scrollbar.pack(side="right", fill="y")
		tk.Button(master, text="Import to GIMP", command= lambda : open_image_gimp("conuhacks.png")).pack(side="top")
		#tk.Button(master, image=PhotoImage(file=image)).pack(side="top")

	def search(self, *args):
		text_to_search = self.entry.get()
		print(text_to_search)

root = tk.Tk()
ss_gui = ShutterStockGUI(root)

root.mainloop()
