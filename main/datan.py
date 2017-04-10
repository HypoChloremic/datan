# Data Analysis
# Analyzes stock information, for investment opportunities and general maintenance
# of user defined portfolios. 
# by Ali Rassolie


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure 
# from os.path import abspath
import requests, csv, pygubu, algo
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import urllib.request as re

class Datan:

	def __init__(self, master):
		# Root definition
		self.master = master # De facto self.root
		self.builder = builder = pygubu.Builder() # This is required to pull the different objects
		builder.add_from_file("gui.ui") # Adds the gui.ui file, such that we may use it. 
		self.mainwindow = builder.get_object('root', master) # This is the master frame in the Tk. 
		
		# The get_object("name") allows to have a variable x point to the object (e.g. frame), 
		# so as to allow further manipulation
		
		
	# Widgets
		
		## Buttons
		self.b1 = builder.get_object("Button_1")
		self.b2 = builder.get_object("Button_2")
		# configuring the buttons
		self.b1.config(command=self.button_1)	
		self.b2.config(command=self.button_2)
		
		## Listboxes
		self.cb1 = builder.get_object("cb1")
		# configuring the comboboxes
		self.cb1.configure(state="readonly")
		self.comboBoxEntry = ["leastSquares", "Mugabeh"]
		self.comboBoxEntryFunctions = [algo.Algo.leastSquares]
		self.cb1["values"] = self.comboBoxEntry

	# Frame
	# Matplotlib
		# Figure
		# We name the graph frame self.graph, such that we can parse it into the matwidget function
		# which in turn paints the matplotlib canvas in the given frame. 
		self.graph = builder.get_object("graph")
		master = self.graph
		
		self.f = Figure(figsize=(6, 7.5))
		self.a = self.f.add_subplot(111)
		self.a2 = self.f.add_subplot(111)
		
		# Canvas
		self.canvas = FigureCanvasTkAgg(self.f, master=master)
		# canvas.show()
		self.canvas.get_tk_widget().grid(column=0, columnspan=30, row=0)

		# Toolbar
		toolbar = NavigationToolbar2TkAgg(self.canvas, master)
		toolbar.update()
		self.canvas._tkcanvas.grid(column=0, row=1)
		toolbar.grid(column=0, row=2)
	

	def urls(self):
		# TODO
		pass

	def button_1(self):
		self.draw()
	

	def button_2(self):
		algoIndex = self.cb1.current()
		self.algo(algoIndex)

	def algo(self, index=None):
		# This is a makeshift solution, a more attractive one will be considered later
		if index==0:
			solutionArray = self.comboBoxEntryFunctions[0](self, x=self.x,y=self.y, order=1)
			# This clears subplot a and shows subplot a2 instead. 
			self.a.cla()
			self.a2.plot(solutionArray)
			self.canvas.show()
		
	def data(self):
		self.yahoo = 'http://ichart.finance.yahoo.com/table.csv?s=AAPL&c=1962'
		with requests.Session() as s:
			download = s.get(self.yahoo)
			decoded_content = download.content.decode('utf-8')
			cr = csv.reader(decoded_content.splitlines(), delimiter=',')
			return list(cr)

	def draw(self):
		# This is some intuitive stuff; we are visualizing the data
		data = self.data()
		self.x = [float(z) for z in range(1,len(data))]
		self.y = [float(data[z][1]) for z in range(1,len(data))]
		
		x = np.array(self.x)
		y = np.array(self.y)
		
		# It does not suffice with only calling the plot method to update the graph, 
		# but we had to draw it via canvas
		self.a.plot(x,y)
		self.canvas.draw()

if __name__ == '__main__':
	root = tk.Tk()
	app = Datan(root)
	root.mainloop()