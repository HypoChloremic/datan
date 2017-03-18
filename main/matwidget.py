import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 

class graph:
	def __init__(self, master=None, **kw):
	# Frame
	# Matplotlib
		# Figure
		f = Figure(figsize=(6, 7.5))
		a = f.add_subplot(111)

		# Canvas
		canvas = FigureCanvasTkAgg(f, master=master)
		canvas.show()
		canvas.get_tk_widget().grid(column=0, columnspan=30, row=0)

		# Toolbar
		toolbar = NavigationToolbar2TkAgg(canvas, master)
		toolbar.update()
		canvas._tkcanvas.grid(column=0, row=1)
		toolbar.grid(column=0, row=2)
	