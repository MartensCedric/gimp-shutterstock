from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import subprocess
import requests
import json
import urllib.request
import getpass
import os
import math
import threading

ss_gui = None
new_search_bool = True
search_timer = None

# make dir before downloading
directory = '/home/' + getpass.getuser() + '/.gimp-2.8/plug-ins/gui/cache'

if not os.path.exists(directory):
	os.makedirs(directory)

def open_image_gimp(path):
	ss_gui.master.destroy()
	subprocess.Popen("gimp {}".format(path).split(), stdout=subprocess.PIPE).communicate()

class SearchResult():
	def __init__(self, path, root):
		self.root = root
		self.path = path

	def open_image(self):
		open_image_gimp(self.path)

	def pop_up(self, event):
		popup = Menu(self.root, tearoff=0)
		popup.add_command(label=self.path)  # , command=next) etc...
		popup.add_command(label="Previous")
		popup.add_separator()
		popup.add_command(label="Home")
		# display the popup menu
		try:
			popup.tk_popup(event.x_root, event.y_root, 0)
		finally:
			# make sure to release the grab (Tk 8.0a1 only)
			popup.grab_release()


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
		global search_timer
		if search_timer is not None:
			search_timer.cancel()

		query = self.entry.get()
		if query == "":
			return

		def start_search():
			# response is in JSON format
			for child in self.scrollable_frame.winfo_children():
				child.destroy()
			t = threading.Thread(target=fetch_images, args=(per_page, current_page))
			t.start()

		search_timer = threading.Timer(0.5, start_search)
		search_timer.start()
		per_page = '12'
		current_page='1'


		def getPreview(imageList, image):
			return imageList[image]['assets']['preview']['url']

		def getPreview_1500(imageList, image):
			return imageList[image]['assets']['preview_1500']['url']

		def fetch_images(per_page, current_page):
			url = "https://api.shutterstock.com/v2/images/search?query="
			# api handling
			headers = {
				'Content-Type': 'application/x-www-form-urlencoded',
				'Authorization': 'Basic ZTYzSGxneHlXTFpVM3BtcXBqcVpWU0FLWUZhTW1OODQ6bThGTEZiUTJFdEw4cVdobg=='
			}
			response = requests.request("GET", url + query + '&per_page=' + per_page + '&page=' + current_page,
										headers=headers)
			imageList = json.loads(response.text)['data']

			for i in range(len(imageList)):
				col_count = 2
				col = i % col_count
				row = math.floor(i / col_count)
				url = getPreview(imageList, i)
				filename = directory + '/img' + str(i) + '.png';
				print(filename)
				t = threading.Thread(target=download_image, args=(row, col, url, filename))
				t.start()

		def download_image(row, col, url, filename):
			urllib.request.urlretrieve(url, filename)
			image = Image.open(filename)
			image = image.resize((390, 390), Image.ANTIALIAS)
			photo = ImageTk.PhotoImage(image)
			label = tk.Label(self.scrollable_frame, image=photo)
			label.img = photo  # this line is not always needed, but include it anyway to prevent bugs
			label.grid(row=row, column=col)
			search_res = SearchResult(filename, label)
			label.bind("<Button-1>", lambda event: search_res.open_image())
			label.bind("<Button-3>", lambda event: search_res.pop_up(event))

	def clear_search_bar(self, *args):
		global new_search_bool
		if new_search_bool:
			self.entry.delete(0, END)
			new_search_bool = False

root = tk.Tk()
ss_gui = ShutterStockGUI(root)
root.mainloop()
