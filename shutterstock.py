#!/usr/bin/env python

from gimpfu import *
import os


def start():
	os.system("python3 ~/.gimp-2.8/plug-ins/shutterstock_gui.py")
	return

register(
	"helloWorldPlugin",

	#blurb
	"Saying Hello World",

	#help
	"Saying Hello to the World",

	#author
	"William Crandell <william@crandell.ws>",

	#copyright
	"William Crandell <william@crandell.ws>",

	#date
	"2015",

	#menupath
	"Hello World",

	#imagetypes (use * for all, leave blank for none)
	"",

	#params
	[],

	#results
	[],

	#function (to call)
	start,

	#this can be included this way or the menu value can be directly prepended to the menupath
	menu = "<Toolbox>/Hello/")

main()
