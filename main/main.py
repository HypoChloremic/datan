import tkinter as tk
import pygubu
import numpy as np
import matwidget
import urllib.request as re
import csv
import requests


class googlefinance:


	def __init__(self, master):
		# Root definition
		self.master = master # De facto self.root
		self.builder = builder = pygubu.Builder() # This is required to pull the different objects
		builder.add_from_file("gui.ui") # Adds the gui.ui file, such that we may use it. 
		self.mainwindow = builder.get_object('root', master) # This is the master frame in the Tk. 
		
		# The get_object("name") allows to have a variable x point to the object (e.g. frame), 
		# so as to allow further manipulation

		self.path  = builder.get_object("pathchooserinput1")
		
		# We name the graph frame self.graph, such that we can parse it into the matwidget function
		# which in turn paints the matplotlib canvas in the given frame. 
		self.graph = builder.get_object("graph")
		self.data()
		matwidget.graph(self.graph, self.data)
	
	def urls(self):
		# TODO
		pass
			
	def data(self):
		self.yahoo = 'http://ichart.finance.yahoo.com/table.csv?s=AAPL&c=1962'
		with requests.Session() as s:
			download = s.get(self.yahoo)
			decoded_content = download.content.decode('utf-8')
			cr = csv.reader(decoded_content.splitlines(), delimiter=',')
			self.data = list(cr)


if __name__ == '__main__':
	root = tk.Tk()
	app = googlefinance(root)
	root.mainloop()
