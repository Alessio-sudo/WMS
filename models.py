from datetime import datetime
from app import db

class User(db.Model):
    _tablename_ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    departments = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # Tolta la virgola fuori posto
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Corretto da 'defalut' a 'default'

    def _repr_(self):
        return f'<User {self.username}>'

class Codici(db.Model):
    _tablename_ = 'codici'

    id = db.Column(db.Integer, primary_key=True)
    codice = db.Column(db.String(255), unique=True, nullable=False)
    descrizione = db.Column(db.Text, nullable=False)
    tipologia = db.Column(db.String(255), nullable=False)
    ubicazione = db.Column(db.String(255), nullable=False)

    def _repr_(self):
        return f'<Codici {self.codice}>'  # Corretto 'self.codici' in 'self.codice'

class PezziMancanti(db.Model):
    _tablename_ = 'pezzi_mancanti'  # Di solito per convenzione i nomi delle tabelle sono in minuscolo

    id = db.Column(db.Integer, primary_key=True)
    codice = db.Column(db.String(255), nullable=False)
    quantita = db.Column(db.String(255), nullable=False)
    stato = db.Column(db.String(255), nullable=False)
    arrivo = db.Column(db.String(255), nullable=False)
    rda = db.Column(db.String(255), nullable=False)
    nota = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def _repr_(self):
        return f'<PezziMancanti {self.codice}>'  # Corretto 'self.mancanti' in 'self.codice'