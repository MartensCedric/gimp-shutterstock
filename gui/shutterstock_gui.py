from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import subprocess
import urllib.request
import getpass
import os
import math
import api_fncs

ss_gui = None
new_search_bool = True

# make dir before downloading
directory = '/home/' + getpass.getuser() + '/.gimp-2.8/plug-ins/gui/cache'

if not os.path.exists(directory):
	os.makedirs(directory)

def open_image_gimp(path):
	ss_gui.master.destroy()
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

		self.entry = tk.Entry(master, textvariable=string_to_search)
		self.entry.insert(END, 'Click here to search for an image...')
		self.entry.bind("<Button-1>", self.clear_search_bar)
		self.entry.pack(fill=tk.X)

		string_to_search.trace("w", self.search)

		canvas = tk.Canvas(container)
		scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
		self.scrollable_frame = ttk.Frame(canvas)

		self.scrollable_frame.bind(
			"<Configure>",
			lambda e: canvas.configure(
				scrollregion=canvas.bbox("all")
			)
		)
		canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
		canvas.configure(yscrollcommand=scrollbar.set)
		container.pack(fill=tk.BOTH, expand=True)
		canvas.pack(side="left", fill=tk.BOTH, expand=True)
		scrollbar.pack(side="right", fill="y")

		tk.Button(self.master, text="Import to GIMP", command=lambda: open_image_gimp("conuhacks.png")).pack(side="top")

	def search(self, *args):
		print(self.entry.get())
		imageList = getImages(self.entry.get())
		
		
		for i in range(len(imageList)):
			col_count = 2
			col = i % col_count
			row = i / col_count
			url = getPreview(imageList, i)
			filename = directory+'/img'+str(i)+'.png';
			print(filename)
			urllib.request.urlretrieve(url, filename)
			image = Image.open(filename)
			image = image.resize((390, 390), Image.ANTIALIAS)
			photo = ImageTk.PhotoImage(image)
			label = tk.Label(self.scrollable_frame, image=photo)
			label.img = photo  # this line is not always needed, but include it anyway to prevent bugs
			#label.grid(row=row, column=col)
			search_res = SearchResult(filename)
			label.bind("<Button-1>", lambda x: search_res.open_image())

	def clear_search_bar(self, *args):
		global new_search_bool
		if new_search_bool:
			self.entry.delete(0, END)
			new_search_bool = False

root = tk.Tk()
ss_gui = ShutterStockGUI(root)
root.mainloop()
