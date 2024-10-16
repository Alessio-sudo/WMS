from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User  # Assicurati che il modello User sia importato correttamente dal tuo models.py

app = Flask(__name__)

# Configurazione del database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'  # Chiave segreta per le sessioni, mettila in modo sicuro!

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configurazione di Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' 

# Caricamento utente per Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Flask-Login richiede questa funzione per recuperare un utente dalla sessione

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Recuperare i dati dal form di login
        username = request.form['username']
        password = request.form['password']
        
        # Verificare l'utente nel database
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login effettuato con successo!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenziali non valide. Riprova.', 'danger')

    return render_template('login.html')

@app.route('/dashboard')
@login_required  # Protegge la dashboard: solo utenti autenticati possono accedere
def dashboard():
    return render_template('dashboard.html', username=current_user.username)

# Articoli mancanti
@app.route('/mancanti')
@login_required
def mancanti():
    return render_template('mancanti.html')

@app.route('/aggiunta-mancanti')
@login_required
def aggiunta_mancanti():
    return render_template('aggiunta_mancanti.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout effettuato con successo!', 'success')
    return redirect(url_for('login'))

if __name__ == '_main_':
    app.run(host='192.168.10.109', port=5000, debug=True)