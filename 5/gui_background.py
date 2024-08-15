
# Create the main window
root = tk.Tk()
root.title("Tkinter Canvas with Resizable Background Image")

# Set the window size to match the image size
root.geometry("500x500")

# Load the background image
bg_image = Image.open("path_to_your_image.jpeg")
bg_image = ImageTk.PhotoImage(bg_image)

# Create a canvas widget with the same size as the image
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack(fill="both", expand=True)

# Add the background image to the canvas
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Function to resize the canvas when the window size changes
def resize_canvas(event):
    canvas.config(width=event.width, height=event.height)

# Bind the resizing event to the function
canvas.bind("<Configure>", resize_canvas)

# Run the application
root.mainloop()