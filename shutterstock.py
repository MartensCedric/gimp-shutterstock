#!/usr/bin/env python

from gimpfu import *
import os


def start():
	os.system("python3 ~/.gimp-2.8/plug-ins/shutterstock_gui.py")
	return

register(
	"ShutterStockIntegrationPlug",

	#blurb
	"Allows to search the ShutterStock",

	#help
	"What do you need help for??",

	#author
	"The Big Brain Brotherhood",

	#copyright
	"The Big Brain Brotherhood 2020",

	#date
	"2020",

	#menupath
	"Add shutterstock Image",

	#imagetypes (use * for all, leave blank for none)
	"",

	#params
	[],

	#results
	[],

	#function (to call)
	start,

	#this can be included this way or the menu value can be directly prepended to the menupath
	menu = "<Toolbox>/shutterstock/")

main()
