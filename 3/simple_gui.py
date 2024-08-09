from tkinter import *

count = 0

def update_text():
    global count
    count += 1
    label.config(text=f"The button has been clicked {count} times")

# Create the main window
window = Tk()
window.title("This is a window")
window.geometry("300x100")

# Create a label to display the count
label = Label(window, text=f"The button has been clicked {count} times")
label.pack(pady=20)

# Create a button that updates the label when clicked
button = Button(window, text="Click Me", command=update_text)
button.pack(pady=10)

# Create a menu bar
menu_bar = Menu(window)

# Create a "File" menu and add it to the menu bar
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Configure the window to display the menu bar
window.config(menu=menu_bar)

# Start the Tkinter event loop
window.mainloop()
