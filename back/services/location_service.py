"""Modulo de servicios de Location"""

from repositories.location_repository import LocationRepository


class LocationService:
    """Clase de serviços de Request"""

    @staticmethod
    def get_all():
        """Obtem todas as localidades"""
        return LocationRepository.get_all()

    @staticmethod
    def get_by_id(location_id):
        """Obtem uma localidade pelo id"""
        return LocationRepository.get_by_id(location_id)

    @staticmethod
    def create(location):
        """Cria uma localidade"""
        return LocationRepository.create(location)

    @staticmethod
    def update(location):
        """Atualiza uma localidade"""
        return LocationRepository.update(location)

    @staticmethod
    def delete(location_id):
        """Deleta uma localidade"""
        return LocationRepository.delete(location_id)
