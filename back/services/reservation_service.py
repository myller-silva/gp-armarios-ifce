"""Módulo de serviço de reservas"""

from repositories.reservation_repository import ReservationRepository
from services.session_service import SessionService


class ReservationService:
    """Classe de serviço de reservas"""

    @staticmethod
    def get_all():
        """Obtem todas as reservas"""
        return ReservationRepository.get_all()

    @staticmethod
    def get_by_id(reservation_id):
        """Obtem uma reserva pelo id"""
        return ReservationRepository.get_by_id(reservation_id)

    @staticmethod
    def create(reservation):
        """Cria uma reserva"""
        return ReservationRepository.create(reservation)

    @staticmethod
    def get_reservations_filtered(data):
        """Obtem as reservas filtradas"""
        return ReservationRepository.get_reservations_filtered(data)

    @staticmethod
    def get_user_reservation():
        """Obtem as reservas ativas do usuário logado"""
        user = SessionService.get_user()
        data = {"user_id": user["id"], "status": "ativa"}
        reservations = ReservationRepository.get_reservations_filtered(data)
        return reservations[0] if reservations else None
