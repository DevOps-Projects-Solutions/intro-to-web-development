from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']  # Retrieves form data
    return f'Hello, {name}! Thanks for submitting the form.'

if __name__ == '__main__':
    app.run(debug=True)