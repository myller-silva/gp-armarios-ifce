"""Modelos de dados do banco de dados"""

# from app import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""Entidade User"""


class User(db.Model):
    """Modelo de dados para usuários"""

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

    def to_dict(self):
        """Retorna um dicionário com os dados do usuário"""
        return {
            "id": self.id,
            "name": self.username,
            "email": self.email,
            "role": self.role,
        }

    def to_table_row(self):
        """Retorna os dados no formato de uma linha de tabela"""
        return [self.id, self.username, self.email, self.role]


class Location(db.Model):
    """Modelo de dados para localizações dos armários"""

    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)  # Nome do bloco/local
    description = db.Column(db.String(200))  # Detalhes adicionais, opcional

    # Relacionamento
    lockers = db.relationship("Locker", backref="location", lazy=True)

    def __repr__(self):
        return f"<Location {self.name}>"

    def to_dict(self):
        """Converte o modelo Location para um dicionário."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }


"""Entidade Locker"""


class Locker(db.Model):
    """Modelo de dados para armários"""

    __tablename__ = "lockers"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="livre")  # livre, ocupado
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)

    # Relacionamento
    reservations = db.relationship("Reservation", backref="locker", lazy=True)

    def __repr__(self):
        return f"<Locker {self.number} - {self.status} - {self.location.name}>"

    def to_dict(self):
        """Retorna um dicionário com os dados do armário"""
        return {
            "id": self.id,
            "number": self.number,
            "status": self.status,
            "location": self.location.to_dict() if self.location else None,
        }


"""Entidade Reservation"""


class Reservation(db.Model):
    """Modelo de dados para reservas"""

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

    def to_dict(self):
        """Retorna um dicionário com os dados da reserva"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "locker_id": self.locker_id,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "status": self.status,
        }


class Request(db.Model):
    """Modelo de dados para solicitações de armários"""

    __tablename__ = "requests"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)
    request_date = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )
    status = db.Column(
        db.String(20), nullable=False, default="pendente"
    )  # pendente, aprovado, rejeitado
    admin_comment = db.Column(
        db.String(200), nullable=True
    )  # Comentário do admin ao aprovar/rejeitar a solicitação

    # Relacionamento
    user = db.relationship("User", backref="requests", lazy=True)
    location = db.relationship("Location", backref="requests", lazy=True)

    def __repr__(self):
        return f"<Request {self.id} - {self.status}>"

    def to_dict(self):
        """Retorna um dicionário com os dados da solicitação"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "location_id": self.location_id,
            "request_date": self.request_date,
            "status": self.status,
            "admin_comment": self.admin_comment,
        }

    def to_table_row(self):
        """Retorna os dados no formato de uma linha de tabela"""
        return [
            self.id,
            self.location.name if self.location else "N/A",
            self.request_date.strftime("%d/%m/%Y %H:%M"),
            self.status,
        ]
