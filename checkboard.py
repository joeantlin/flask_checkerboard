from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', row = 4, col = 4, html_color1 = 'black', html_color2 = 'red')

@app.route('/<x>/')
def rows(x):
    return render_template('index.html', row = int(x), col = int(x), html_color1 = 'black', html_color2 = 'red')

@app.route('/<x>/<y>')
def rowsandcols(x, y):
    return render_template('index.html', row = int(x), col = int(y), html_color1 = 'black', html_color2 = 'red')

@app.route('/<x>/<y>/<color1>/<color2>')
def colors(x, y, color1, color2):
    return render_template('index.html', row = int(x), col = int(y), html_color1 = color1, html_color2 = color2)

if __name__=='__main__':
    app.run(debug=True)