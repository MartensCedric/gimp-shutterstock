from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import subprocess

ss_gui = None
def open_image(path):
	ss_gui.master.quit
	subprocess.Popen("gimp {}".format(path).split(), stdout=subprocess.PIPE).communicate()

class ShutterStockGUI:
	def __init__(self, master):
		self.master = master
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
		tk.Button(master, text="Import to GIMP", command= lambda : open_image("conuhacks.png")).pack(side="top")
		image = Image.open('conuhacks.png')
		image = image.resize((50, 50), Image.ANTIALIAS)
		photo = ImageTk.PhotoImage(image)
		label = tk.Label(root, image=photo)
		label.img = photo  # this line is not always needed, but include it anyway to prevent bugs
		label.pack()
		#tk.Button(master, image=PhotoImage(file=image)).pack(side="top")

	def search(self):
		print(self.entry.get())

root = tk.Tk()
ss_gui = ShutterStockGUI(root)

root.mainloop()
