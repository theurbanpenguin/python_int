import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Tkinter Canvas with Resizable Background Image")

# Load the background image
bg_image = Image.open("devandcolab.jpegcolab.jpeg")
bg_image = ImageTk.PhotoImage(bg_image)

# Create a canvas widget with the same size as the image
canvas = tk.Canvas(root, width=bg_image.width(), height=bg_image.height())
canvas.pack(fill="both", expand=True)

# Add the background image to the canvas
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Optional: Add more widgets or drawings to the canvas
# canvas.create_text(100, 50, text="Welcome to Corporate Dashboard", fill="white", font=("Helvetica", 24))

# Function to resize the canvas when the window size changes
def resize_canvas(event):
    canvas.config(width=event.width, height=event.height)

# Bind the resizing event to the function
canvas.bind("<Configure>", resize_canvas)

# Run the application
root.mainloop()
