"""Modulo de servicios de Request"""

from repositories.request_repository import RequestRepository
from models import Request
from services.session_service import SessionService


class RequestService:
    """Clase de serviços de Request"""

    @staticmethod
    def get_all_requests():
        """Obtem todos os pedidos"""
        return RequestRepository.get_all_requests()

    @staticmethod
    def get_request_by_id(request_id):
        """Obtem um pedido pelo id"""
        return RequestRepository.get_request_by_id(request_id)

    @staticmethod
    def create_user_request(location_id):
        """Cria um requisição de usuário"""
        user = SessionService.get_user()
        request = Request(
            user_id=user["id"],
            location_id=location_id,
        )
        return RequestRepository.create_request(request)

    @staticmethod
    def update_request(request):
        """Atualiza um pedido"""
        return RequestRepository.update_request(request)

    @staticmethod
    def delete_request(request_id):
        """Deleta um pedido"""
        return RequestRepository.delete_request(request_id)

    @staticmethod
    def get_requests_filtered(data):
        """Obtem pedidos filtrados"""
        return RequestRepository.get_requests_filtered(data)
