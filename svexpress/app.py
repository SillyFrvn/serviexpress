from flask import Flask, render_template, request, redirect, session

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

@app.route('/miembros')
def miembros():
    return render_template('miembros.html')

#LOGIN

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['logged_in'] = True
            session['username'] = username 
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='credenciales incorrectas')
    return render_template('login.html')
    
#acceso al dashboard
@app.route('/dashboard')
def dashboard():
    
        return render_template('dashboard.html')
    

#ruta del logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/informe')
def informe():
    return render_template('informe.html')

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)


    #BASE DE DATOS 
    users = {
    'user1': {'username': 'admin', 'password': 'admin'},
    'user2': {'username': 'user', 'password': 'user'}
}