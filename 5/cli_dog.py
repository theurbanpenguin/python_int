import requests

# URL for the API that provides a random dog image
url = "https://dog.ceo/api/breeds/image/random"

# Make the GET request to the API
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Get the image URL from the response
image_url = data['message']

# Download the image
image_response = requests.get(image_url)

# Define the file name and save the image
with open("random_dog.jpg", "wb") as file:
    file.write(image_response.content)

print("Image downloaded successfully as random_dog.jpg")