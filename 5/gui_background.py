import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Tkinter Canvas with Resizable Background Image")

# Set the window size to match the image size
root.geometry("500x500")

# Load the background image
bg_image = Image.open("image.jpg")
bg_image = ImageTk.PhotoImage(bg_image)

# Create a Label to hold the background image
# A canvas can take an image but other widgets can't go on top of the canvas
background_label = tk.Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create an Exit button and place it on the label
exit_button = tk.Button(root, text="Exit", bg="red", fg="white", command=root.quit)
exit_button.place(x=450, y=450)  # Position the button at the bottom-right corner

# Run the application
root.mainloop()
