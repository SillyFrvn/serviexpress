from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/mecanicos')
def mecanicos():
    return render_template('mecanicos.html')

@app.route('/reserva')
def reserva():
    return render_template('toma_horas.html')



if __name__ == '__main__':
    app.run(debug=True)