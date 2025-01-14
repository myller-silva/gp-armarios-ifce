from datetime import datetime, timedelta
from flask import redirect, url_for
from models import db, Request, Locker, Reservation
# from flask_login import current_user

class LockerRequestService:
    @staticmethod
    def process_requests(status_updates):
        """Processa as alterações de status das solicitações."""
        for req_id, status in status_updates.items():
            locker_request = Request.query.get(req_id)
            if locker_request:
                locker_request.status = status
                # Se a solicitação for aceita, atribuir um armário
                if status == 'aprovado':
                    LockerRequestService.assign_locker(locker_request)
        db.session.commit()

    @staticmethod
    def assign_locker(locker_request):
        """Atribui um armário para a solicitação aceita."""
        locker = Locker.query.filter_by(location_id=locker_request.location.id, status='livre').first()
        if locker:
            locker.status = 'ocupado'
            locker.user_id = locker_request.user_id  # Atribui o armário ao usuário
            locker_request.status = 'aprovado'  # Atualiza o status da solicitação
            locker_request.locker_id = locker.id  # Armazena o ID do armário na solicitação
            
            # Cria uma reserva para o usuário
            reservation = Reservation(
                user_id=locker_request.user_id,
                locker_id=locker.id,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=30),
                status='ativa'
            )
            db.session.add(reservation)
            db.session.commit()

    @staticmethod
    def get_pending_requests():
        """Obtém as solicitações pendentes."""
        return Request.query.filter_by(status='pendente').all()
