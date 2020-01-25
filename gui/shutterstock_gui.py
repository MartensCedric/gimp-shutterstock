from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import subprocess

ss_gui = None
new_search_bool = True

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

		top_image = Image.open('gui/title.jpg')
		top_photo = ImageTk.PhotoImage(top_image)
		top_label = tk.Label(master, image=top_photo)
		#load = Image.open("gui/title.jpg")
		#render = ImageTk.PhotoImage(load)
		#img = tk.Label(master, image=render)
		#img.place(x = 0, y = 0)

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
		#print(text_to_search)

	def clear_search_bar(self, *args):
		global new_search_bool
		if(new_search_bool):
			self.entry.delete(0, END)
			new_search_bool = False
	

root = tk.Tk()
ss_gui = ShutterStockGUI(root)

root.mainloop()
