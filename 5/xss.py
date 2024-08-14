from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the user input
        user_input = request.form.get('user_input')

        # Render a template with user input (this is intentionally vulnerable to XSS)
        return render_template_string(f"""
            <h1>XSS Demonstration</h1>
            <p>You entered: {user_input}</p>
            <a href="/">Go Back</a>
            """)
    else:
        # Render a simple form
        return render_template_string("""
            <h1>XSS Demonstration</h1>
            <form method="POST">
                <label for="user_input">Enter something:</label>
                <input type="text" id="user_input" name="user_input">
                <button type="submit">Submit</button>
            </form>
            """)


if __name__ == '__main__':
    app.run(debug=True)
