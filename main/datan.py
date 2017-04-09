# Data Analysis
# Analyzes stock information, for investment opportunities and general maintenance
# of user defined portfolios. 
# by Ali Rassolie
# Contributions by August Heddini, Justin Smertinas, and Isak Persson. 


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import pygubu
import urllib.request as re
import csv
import requests
from os.path import abspath

class Datan:

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
		# Frame
		self.graph = builder.get_object("graph")
		
		# Buttons
		self.b1 = builder.get_object("Button_2")
		self.b1.config(command=self.button_2)


	# Frame
	# Matplotlib
		# Figure
		self.f = Figure(figsize=(6, 7.5))
		self.a = self.f.add_subplot(111)
		master = self.graph
		
		# Canvas
		canvas = FigureCanvasTkAgg(self.f, master=master)
		canvas.show()
		canvas.get_tk_widget().grid(column=0, columnspan=30, row=0)

		# Toolbar
		toolbar = NavigationToolbar2TkAgg(canvas, master)
		toolbar.update()
		canvas._tkcanvas.grid(column=0, row=1)
		toolbar.grid(column=0, row=2)
	

	def urls(self):
		# TODO
		pass

	def button_2(self):
		self.data()
		self.draw()

	def data(self):
		self.yahoo = 'http://ichart.finance.yahoo.com/table.csv?s=AAPL&c=1962'
		with requests.Session() as s:
			download = s.get(self.yahoo)
			decoded_content = download.content.decode('utf-8')
			cr = csv.reader(decoded_content.splitlines(), delimiter=',')
			self.data = list(cr)

	def draw(self):
		data = self.data
		print(len(data))
		x = []
		y = []
		for k in range(1, len(data)):
			x.append(k)
			y.append(float(data[k][1]))
			print(data[k][1])
		x = np.array(x, float)
		y = np.array(y, float)
		self.a(x,y)


class graph:
	def __init__(self, master=None, data=None, condition=False, **kw):
	# Frame
	# Matplotlib
		# Figure
		self.f = Figure(figsize=(6, 7.5))
		self.a = f.add_subplot(111)
		
		# Canvas
		canvas = FigureCanvasTkAgg(self.f, master=master)
		canvas.show()
		canvas.get_tk_widget().grid(column=0, columnspan=30, row=0)

		# Toolbar
		toolbar = NavigationToolbar2TkAgg(canvas, master)
		toolbar.update()
		canvas._tkcanvas.grid(column=0, row=1)
		toolbar.grid(column=0, row=2)

	def draw(self):
		data = data
		print(len(data))
		x = []
		y = []
		for k in range(1, len(data)):
			x.append(k)
			y.append(float(data[k][1]))
			print(data[k][1])
		
		x = np.array(x, float)
		y = np.array(y, float)



if __name__ == '__main__':
	root = tk.Tk()
	app = Datan(root)
	root.mainloop()