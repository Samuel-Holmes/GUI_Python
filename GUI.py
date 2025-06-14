# Graphical user interface within the python programming language 

from tkinter import * 

# Creating the window

window = Tk()

# This is the title at the top of the window similar to a tab title within HTML

window.title('My first GUI')

# This label is created and then must be placed within the window itself

label = Label(window, text = 'Hello World!')

# For placing the label I have used place which takes both XY coordinates, however there is also pack and grid options 

label.place(x= 50, y = 50)


window.mainloop()