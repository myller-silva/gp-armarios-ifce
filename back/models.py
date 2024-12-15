"""Modelos de dados do banco de dados"""

# from app import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""Entidade User"""


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="aluno")  # aluno, admin

    # Relacionamento
    reservations = db.relationship("Reservation", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"


"""Entidade Locker"""


class Locker(db.Model):
    __tablename__ = "lockers"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="livre")  # livre, ocupado

    # Relacionamento
    reservations = db.relationship("Reservation", backref="locker", lazy=True)

    def __repr__(self):
        return f"<Locker {self.number} - {self.status}>"


"""Entidade Reservation"""


class Reservation(db.Model):
    __tablename__ = "reservations"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    locker_id = db.Column(db.Integer, db.ForeignKey("lockers.id"), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(
        db.String(20), nullable=False, default="ativa"
    )  # ativa, cancelada

    def __repr__(self):
        return f"<Reservation {self.id} - {self.status}>"
