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
		## Labels
		self.l1 = builder.get_object("Label_1")
		self.l2 = builder.get_object("Label_2")
		self.l3 = builder.get_object("Label_3")
		# configuring labels
		self.infobox = ""

		## Buttons
		self.b1 = builder.get_object("Button_1")
		self.b2 = builder.get_object("Button_2")
		# configuring the buttons
		self.b1.config(command=self.button_1)	
		self.b2.config(command=self.button_2)
		
		## Comboboxes
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
	
	# File dialog options
		# define options for opening or saving a file
		self.file_opt = options = {}
		options['defaultextension'] = '.txt'
		options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
		options['initialdir'] = 'C:\\Users\\Ali Rassolie\\OneDrive\\prwork\\python\\programs\\datan\\main'
		options['parent'] = self.master
		options['title'] = 'This is a title'


	def urls(self):
		# TODO
		pass

	def button_1(self):
		# This opens a dialog option, so as to allow user to select file
		fileName = tk.filedialog.askopenfile(**self.file_opt)
	
		# fileName is already an opened file; which implies that we can read write already
		# We want to split the string, and make an accessible list by index
		content = fileName.read().split()
		
		# As we will have to handle the api differently if we have several companies in the portfolio, 
		# we will need to differentiate between one selected company and several. 
		if len(content) > 1:
			self.portfolio = True
			self.draw(portfolio=True)
		
		elif len(content) == 1:
		# Having completed the selection process, we can go onto drawing it
			self.fileCompany = content[0]
			self.portfolio = False
			self.draw(portfolio=False)
		else: 
			raise Exception("The portfolio did not work outS")


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
		
	def data(self, portfolio=False):
		if portfolio is False:
			company = self.fileCompany
			self.yahoo = 'http://ichart.finance.yahoo.com/table.csv?s=%s&c=1962' % company
			with requests.Session() as s:
				download = s.get(self.yahoo)
				decoded_content = download.content.decode('utf-8')
				cr = csv.reader(decoded_content.splitlines(), delimiter=',')
				return list(cr)
		else: 
			# Todo
			pass

	def draw(self, portfolio=False):
		# This is some intuitive stuff; we are visualizing the data
		data = self.data(portfolio=portfolio)
		self.x = [float(z) for z in range(1,len(data))]
		self.y = [float(data[z][1]) for z in range(1,len(data))]
		
		x = np.array(self.x)
		y = np.array(self.y)
		
		# It does not suffice with only calling the plot method to update the graph, 
		# but we had to draw it via canvas
		self.a.plot(x,y)
		self.canvas.draw()
		self.update_info(portfolio=self.portfolio)

	def update_info(self, portfolio=False):
		# This will update the infobox
		# Here the portfolio condition is pretty important, as it is everywhere to be honest
		if portfolio is True:
			pass
		elif:
			self.infobox = self.infobox + "\nCompany Name: %s" % self.fileCompany 
			self.l3.config(text=self.infobox)
		else:
			raise Exception("Infobox issue it seems; might be associated with the portfolio condition")
if __name__ == '__main__':
	root = tk.Tk()
	app = Datan(root)
	root.mainloop()