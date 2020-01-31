import numpy as np
from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'] )
def ergebnis():
    feld1 = ""
    feld2 = ""
    if request.method == 'POST':
        feld1 = request.form['feld1']
        feld2 = request.form['feld2']
        inhalt1 = int(feld1)
        inhalt2 = int(feld2)
        erg = np.lcm(inhalt1, inhalt2)
        kgV = str(erg)
    return render_template('index.html', zahl1= inhalt1, zahl2= inhalt2, ergebnis= kgV)


if __name__=='__main__':
    app.run(port=1337, debug=True)