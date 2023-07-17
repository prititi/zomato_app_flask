from flask import Flask, render_template, request, redirect

app = Flask(__name__)

data = {}  # Dictionary to store the data

@app.route('/')
def home():
    return redirect('/read')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        data[key] = value
        return redirect('/read')
    return render_template('create.html')

@app.route('/read')
def read():
    return render_template('read.html', data=data)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            value = request.form['value']
            data[key] = value
        return redirect('/read')
    return render_template('update.html', data=data)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            del data[key]
        return redirect('/read')
    return render_template('delete.html', data=data)

if __name__ == '__main__':
    app.run()
