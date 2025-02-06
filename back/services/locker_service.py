"""Serviço para manipulação de armários."""

from models import Locker, Location
from flask import session
# from services.reservation_service import ReservationService

class LockerService:
    """Classe de serviço de armários"""

    @staticmethod
    def get_all():
        """Obtem todos os armários"""
        return Locker.query.all()

    @staticmethod
    def get_by_id(locker_id):
        """Obtem um armário pelo id"""
        return Locker.query.get(locker_id)

    @staticmethod
    def get_by_location(location_id):
        """Obtem os armários de uma localidade"""
        return Locker.query.filter_by(location_id=location_id).all()
    
    @staticmethod
    def calculate_availability():
      """
      Calcula a disponibilidade de armários para todas as localizações (blocos).

      Returns:
          list: Lista de dicionários contendo os dados de disponibilidade de cada localização.
      """
      # Consulta todas as localizações (blocos)
      locations = Location.query.all()

      # Cria uma lista para armazenar as informações de cada bloco
      availability_data = []

      for location in locations:
          total_lockers = len(location.lockers)
          free_lockers = sum(1 for locker in location.lockers if locker.status == "livre")

          # Calcula o percentual de armários livres
          percent_free = (free_lockers / total_lockers * 100) if total_lockers > 0 else 0

          # Adiciona os dados do bloco na lista
          availability_data.append(
              {
                  "location_dict": location.to_dict(),
                  "total_lockers": total_lockers,
                  "free_lockers": free_lockers,
                  "percent_free": round(percent_free, 2),
              }
          )

      return availability_data
    # @staticmethod
    # def create(locker):
    #     """Cria um armário"""
    #     db.session.add(locker)
    #     db.session.commit()
    #     return locker

    # @staticmethod
    # def update(locker):
    #     """Atualiza um armário"""
    #     db.session.commit()
    #     return locker

    # @staticmethod
    # def delete(locker_id):
    #     """Deleta um armário"""
    #     locker = Locker.query.get(locker_id)
    #     if locker:
    #         db.session.delete(locker)
    #         db.session.commit()
    #         return locker
    #     return None

    # @staticmethod
    # def get_user_locker(user_id):
    #     """Obtem o armário de um usuário"""
    #     reservation = Reservation.query.filter_by(user_id=user_id, status="ativa").first()
    #     if reservation:
    #         return reservation.locker
    #     return None