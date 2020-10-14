from tkinter import Frame, Label, Button, Entry, DoubleVar, StringVar
from tkinter.messagebox import showwarning
from model import clf, feature_names, target_names

class IrisGUI(Frame):
	def __init__(self, parent=None):
		self.measurements = []
		super().__init__(parent)
		self.pack(expand='yes', fill='both')
		self.make_widgets()

	def make_form(self):
		form = Frame(self, relief='raised', border=2)
		left = Frame(form)
		right = Frame(form)
		form.pack(fill='both')
		left.pack(side='left')
		right.pack(side='right', expand='yes', fill='both')

		for feature in feature_names:
			lab = Label(left, width=15, text=feature+':')
			ent = Entry(right)
			lab.pack(side='top')
			ent.pack(side='top', pady=.5, expand='yes', fill='both')
			var = DoubleVar()
			ent.config(textvariable=var)
			var.set('0.0')
			self.measurements.append(var)


	def output(self):
		form = Frame(self, relief='raised', border=2)
		bottom = Frame(form)
		form.pack(fill='both')
		bottom.pack(side='bottom', expand='yes', fill='both')
		lab = Label(bottom, width=10, text='outcome:')
		ent = Entry(bottom)
		lab.pack(side='left')
		ent.pack(side='right', expand='yes', fill='both')
		self.var = StringVar()
		ent.config(textvariable=self.var)

	def get_measurements(self):
		measurements = []
		try:
			for var in self.measurements:
				measurements.append(var.get())
			return measurements
		except Exception:
			showwarning("Invalid input", "Ensure all inputs are correct")

	def make_widgets(self):
		self.make_form()
		button = Button(self, text='Predict', command=self.predict)
		button.pack(side='bottom')
		self.output()
	
	def predict(self):
		measurements = self.get_measurements()
		#print(measurements)
		if len(measurements)<4:
			showwarning("No input", "Ensure all input boxes are filled.")
		outcome = clf.predict([measurements])[0]
		#print(outcome)
		if outcome==0:
			self.var.set('iris-'+target_names[0])
		elif outcome==1:
			self.var.set('iris-'+target_names[1])
		else:
			self.var.set('iris-'+target_names[2])


if __name__ == "__main__":
	from tkinter import Tk
	root = Tk()
	root.title("Predict Iris Flower")
	root.minsize(width=300, height=140)
	IrisGUI(root)
	root.mainloop()