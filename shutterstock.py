#!/usr/bin/env python

from gimpfu import *
import os


def start():
	os.system("python3 ~/.gimp-2.8/plug-ins/gui/shutterstock_gui.py")
	return

register(
	"ShutterstockIntegration",

	#blurb
	"Add an image from the Shutterstock API",

	#help
	"Who needs help?",

	#author
	"The Big Brain Brotherhood",

	#copyright
	"The Big Brain Brotherhood 2020",

	#date
	"2020",

	#menupath
	"Add Shutterstock image",

	#imagetypes (use * for all, leave blank for none)
	"",

	#params
	[],

	#results
	[],

	#function (to call)
	start,

	#this can be included this way or the menu value can be directly prepended to the menupath
	menu = "<Toolbox>/Shutterstock/")

main()
