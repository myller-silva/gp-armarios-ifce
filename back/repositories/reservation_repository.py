"""Módulo de repositório de reservas"""

from models import db, Reservation


class ReservationRepository:
    """Classe de repositório de reservas"""

    @staticmethod
    def get_all():
        """Obtem todas as reservas"""
        return Reservation.query.all()

    @staticmethod
    def get_by_id(reservation_id):
        """Obtem uma reserva pelo id"""
        return Reservation.query.get(reservation_id)

    @staticmethod
    def create(reservation):
        """Cria uma reserva"""
        db.session.add(reservation)
        db.session.commit()
        return reservation
    
    @staticmethod
    def get_reservations_filtered(data):
        """Obtem as reservas filtradas"""
        query = Reservation.query
        if "location_id" in data:
            query = query.filter_by(location_id=data["location_id"])
        if "status" in data:
            query = query.filter_by(status=data["status"])
        if "user_id" in data:
          query = query.filter_by(user_id=data["user_id"])
        if "start_date" in data:
          query = query.filter(Reservation.start_date >= data["start_date"])
        if "end_date" in data:
          query = query.filter(Reservation.end_date <= data["end_date"])
        return query.all()
