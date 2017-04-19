# Data Analysis
# Analyzes stock information, for investment opportunities and general maintenance
# of user defined portfolios. 
# by Ali Rassolie
# Tested with Python 3.5.2

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure 
from dataHandler import DataHandler
import pygubu, algo
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import urllib.request as re

class Datan:

	def __init__(self, master=None):

		# Misc definitions
		self.stock_attribute = ""


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
		self.b3 = builder.get_object("Button_3")
		self.b4 = builder.get_object("Button_5")
		self.b5 = builder.get_object("Button_6")
		self.save = builder.get_object("save")
		# configuring the buttons
		self.b1.config(command=self.button_1)	
		self.b2.config(command=self.button_2)
		self.b3.config(command=self.button_3)
		self.b4.config(command=self.button_4)
		self.b5.config(command=self.button_5)
		self.save.config(command=self.save_button)	
		## Comboboxes
		self.cb1 = builder.get_object("cb1")
		self.cb2 = builder.get_object("cb2")
		self.cb3 = builder.get_object("cb3")
		# configuring the comboboxes
		self.cb1.configure(state="readonly")
		self.comboBoxEntry = ["leastSquares", "Mugabeh"]
		self.comboBoxEntryFunctions = [algo.Algo.leastSquaresApproximationResults]
		self.cb1["values"] = self.comboBoxEntry

		self.cb2.configure(state="readonly")
		self.comboBoxEntry_2 = ["30d", "60d", "120d", "1y", "3y", "5y"]
		self.cb2["values"] = self.comboBoxEntry_2

		self.cb3.configure(state="readonly")
		self.comboBoxEntry_3 = ["open", "close", "high", "low", "open/close", "high/low"]
		self.cb3["values"] = self.comboBoxEntry_3
		
		## Entry
		self.e1 = builder.get_object("Entry_1")
		self.e2 = builder.get_object("Entry_2")
		self.e3 = builder.get_object("Entry_3")
		self.e4 = builder.get_object("Entry_4") 

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
		self.canvas.get_tk_widget().grid(column=0, columnspan=30, row=0)
		self.canvas._tkcanvas.grid(column=0, row=1)

		# Toolbar
		toolbar = NavigationToolbar2TkAgg(self.canvas, master)
		toolbar.update()
		toolbar.grid(column=0, row=2)
	
	# File dialog options
		# define options for opening or saving a file
		self.file_opt = options = {}
		options['defaultextension'] = '.txt'
		options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
		options['initialdir'] = 'C:\\Users\\Ali Rassolie\\OneDrive\\prwork\\python\\programs\\datan\\main'
		options['parent'] = self.master
		options['title'] = 'This is a title'

	def button_1(self):
		# This opens a dialog option, so as to allow user to select file
		fileName = tk.filedialog.askopenfile(**self.file_opt)
	
		# fileName is already an opened file; which implies that we can read write already
		# We want to split the string, and make an accessible list by index
		content = fileName.read().split()
		
		# As we will have to handle the api differently if we have several companies in the portfolio, 
		# we will need to differentiate between one selected company and several. 
		if len(content) > 1:
			self.portfolio = True # This is necessary for the methods that use it as a condition
			self.draw(portfolio=True)
		
		elif len(content) == 1:
		# With only one selected company, continue by running the draw method with portfolio as false. 
			self.fileCompany = content[0] # This points to the first company entry
			self.portfolio = False
			self.draw()
		
		else: 
			raise Exception("The portfolio did not work out")


	def button_2(self):
		# This will be looking up the index for the current algorithm function in the algorithm list
		# It is an actual index that is printed
		self.algoIndex = self.cb1.current()
		self.algo_handler(index = self.algoIndex)

	def button_3(self):
		pass

	def button_4(self):
		try:
			first_entry   = int(self.e3.get())
			second_entry  = int(self.e4.get())
			self.x_wanted = [ x for x in range(first_entry, second_entry, 1) ]
			print(self.x_wanted)
			self.algo_handler(self.x_wanted, index=self.algoIndex)
		
		except ValueError:
			raise Exception("Problem with the type of entry")

	def button_5(self):
		try:
			self.a.cla() # This clears subplot a. This may not be absolutely necessary, but provides a neat way of cleaning the canvas.	
			
			try:
				self.a2.cla()
			
			except Exception as e:
				raise e
		
		except:
			raise Exception("Problem with clear")
	
	def save_button(self):
		pass

	def algo_handler(self, *args, index=None):
		# This is a makeshift solution, a more attractive one will be considered later
		# The index to the company list is being used	
		if index==0 :
			# These are the configurations necessary to run the leastSquares algo
			if args:
				approximated_y_values = self.comboBoxEntryFunctions[0](self, xKnown=self.x, yKnown=self.y, order=2, xWanted=args[0])
				x_wanted = np.array(self.x_wanted)
				approximated_y_values = np.array(approximated_y_values)
				self.a2.plot(self.x_wanted, approximated_y_values)
				self.canvas.show()
			else:
				raise Exception("You got some problems with the args here boyy")
		else:
			raise Exception
		
	def draw(self, portfolio=False, arguments=False, *args):
		# This is some intuitive stuff; we are visualizing the data
		# DataHandler.data will return a list which we then can deal with

		if arguments is False:
			self.x, self.y = DataHandler.data(self, "open", portfolio=portfolio, company=self.fileCompany)
			x = np.array(self.x)
			y = np.array(self.y)

		elif arguments is True:
			self.x, self.y = DataHandler.data(self, self.stock_attribute, portfolio=portfolio, company=self.fileCompany)
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
		
		if portfolio is False:
			self.infobox = self.infobox + "\nCompany Name: %s" % self.fileCompany # storing str of the company name for the user 
			stock_value = self.y
			stock_value.sort()
			max_stock_value, min_stock_value = stock_value[-1], stock_value[0]
			self.infobox = self.infobox + "\nMax: %d\nMin: %d" % (max_stock_value, min_stock_value) # Min Max
			self.l3.config(text=self.infobox) # presenting the information
		
		elif portfolio is True:
			pass
		
		else:
			assert portfolio
			raise Exception("Infobox issue it seems; might be associated with the portfolio condition")
	
	def date_handler(self):
		self.date_of_interest = self.cb2.current() 
		if self.date_of_interest is "30d":
			new_x = self.x[0:30]
			new_y = self.y[0:30]

if __name__ == '__main__':
	root = tk.Tk()
	app = Datan(root)
	root.mainloop()