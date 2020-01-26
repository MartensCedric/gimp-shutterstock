from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import subprocess
import requests
import requests
import json
import urllib.request
import getpass
import os


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

		for r in range(18):
			for c in range(2):
				image = Image.open('conuhacks.png')
				image = image.resize((390, 390), Image.ANTIALIAS)
				photo = ImageTk.PhotoImage(image)
				label = tk.Label(scrollable_frame, image=photo)
				label.img = photo  # this line is not always needed, but include it anyway to prevent bugs
				label.grid(row=r, column=c)
				search_res = SearchResult("conuhacks.png")
				label.bind("<Button-1>", lambda x : search_res.open_image())

		container.pack(fill=tk.BOTH, expand=True)
		canvas.pack(side="left", fill=tk.BOTH, expand=True)
		scrollbar.pack(side="right", fill="y")
		tk.Button(master, text="Import to GIMP", command= lambda : open_image_gimp("conuhacks.png")).pack(side="top")
		#tk.Button(master, image=PhotoImage(file=image)).pack(side="top")

	def search(self):
		print(self.entry.get())
		query = self.entry.get()
		per_page = '12'
		current_page='1'
		url = "https://api.shutterstock.com/v2/images/search?query="
		#api handling
		headers = {
			'Content-Type': 'application/x-www-form-urlencoded',
			'Authorization': 'Basic ZTYzSGxneHlXTFpVM3BtcXBqcVpWU0FLWUZhTW1OODQ6bThGTEZiUTJFdEw4cVdobg=='
		}

		# response is in JSON format
		response = requests.request("GET", url+query + '&per_page=' + per_page + '&page=' + current_page, headers=headers)
		imageList = json.loads(response.text)['data']

		def getPreview(imageList, image):
			return imageList[image]['assets']['preview']['url']

		def getPreview_1500(imageList, image):
			return imageList[image]['assets']['preview_1500']['url']

		#make dir before downloading
		directory = '/home/'+ getpass.getuser() + '/Desktop/tempPics'
		if not os.path.exists(directory):
    		os.makedir(directory)
		
		for img in range(len(imageList)):
			url = getPreview(imageList, img)
			urllib.request.urlretrieve(url, directory+'/img'+str(img)+'.jpg')

	def clear_search_bar(self, *args):
		global new_search_bool
		if(new_search_bool):
			self.entry.delete(0, END)
			new_search_bool = False

root = tk.Tk()
ss_gui = ShutterStockGUI(root)

root.mainloop()
