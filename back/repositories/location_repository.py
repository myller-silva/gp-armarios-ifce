"""Modulo de repositorio de Location"""
from models import db, Location

class LocationRepository:
    """Clase de repositorio de Location"""

    @staticmethod
    def get_all():
        """Obtem todas as localidades"""
        return Location.query.all()

    @staticmethod
    def get_by_id(location_id):
        """Obtem uma localidade pelo id"""
        return Location.query.get(location_id)

    @staticmethod
    def create(location):
        """Cria uma localidade"""
        db.session.add(location)
        db.session.commit()
        return location

    @staticmethod
    def update(location):
        """Atualiza uma localidade"""
        db.session.commit()
        return location

    @staticmethod
    def delete(location_id):
        """Deleta uma localidade"""
        location = Location.query.get(location_id)
        if location:
            db.session.delete(location)
            db.session.commit()
            return location
        return None