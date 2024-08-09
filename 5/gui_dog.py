import requests
from PIL import Image, ImageTk
import tkinter as tk

# URL for the API that provides a random dog image
url = "https://dog.ceo/api/breeds/image/random"

# Make the GET request to the API
response = requests.get(url)
data = response.json()

# Get the image URL from the response
image_url = data['message']

# Download the image
image_response = requests.get(image_url)

# Save the image to a file
with open("random_dog.jpg", "wb") as file:
    file.write(image_response.content)

# Create a Tkinter window
window = tk.Tk()
window.title("Random Dog Image")

# Load the image using PIL and convert to PhotoImage
image = Image.open("random_dog.jpg")
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
label = tk.Label(window, image=photo)
label.pack()

# Start the Tkinter event loop
window.mainloop()