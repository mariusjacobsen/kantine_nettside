from sysconfig import get_default_scheme

from flask import Flask, render_template
from kantinedata import varer

app = Flask(__name__)


@app.route('/')
def hjem():
    return render_template("index.html")

@app.route('/meny')
def meny():
    return render_template("meny.html")

@app.route('/varer')
def vis_varer():
    return render_template("varer.html", varer=varer)

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")

if __name__ == '__main__':
    app.run(debug=True)
