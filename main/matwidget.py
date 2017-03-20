from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

class graph:
	def __init__(self, master=None, data=None):
	# Frame
	# Matplotlib
		# Figure
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


		f = Figure(figsize=(6, 7.5))
		a = f.add_subplot(111)
		a.plot(x, y)
		# Canvas
		canvas = FigureCanvasTkAgg(f, master=master)
		canvas.show()
		canvas.get_tk_widget().grid(column=0, columnspan=30, row=0)

		# Toolbar
		toolbar = NavigationToolbar2TkAgg(canvas, master)
		toolbar.update()
		canvas._tkcanvas.grid(column=0, row=1)
		toolbar.grid(column=0, row=2)
	
