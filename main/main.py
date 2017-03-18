import tkinter as tk
import pygubu
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
import matwidget


class googlefinance:
	def __init__(self, master):
		# Root definition
		self.master = master
		self.builder = builder = pygubu.Builder()
		builder.add_from_file("gui.ui")
		self.mainwindow = builder.get_object('root', master)
		
		# The get_object("name") allows to have a variable x point to the object (e.g. frame), 
		# so as to allow further manipulation
		self.graph = builder.get_object("graph") 
		matwidget.graph(self.graph)		

if __name__ == '__main__':
	root = tk.Tk()
	app = googlefinance(root)
	root.mainloop()


