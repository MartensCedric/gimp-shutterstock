#!/usr/bin/env python

from gimpfu import *
import os
import webbrowser


def start():
	webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
	return

register(
	"ShutterstockLogin",

	#blurb
	"Logs into the Shutterstock API",

	#help
	"Who needs help?",

	#author
	"The Big Brain Brotherhood",

	#copyright
	"The Big Brain Brotherhood 2020",

	#date
	"2020",

	#menupath
	"Log into Shutterstock",

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