from flask import Flask, jsonify

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the default URL, which returns "Hello, World!"
@app.route('/', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!")

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
