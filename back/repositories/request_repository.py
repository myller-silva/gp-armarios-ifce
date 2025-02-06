"""Modulo de repositorio de Request"""

from models import db, Request


class RequestRepository:
    """Clase de repositorio de Request"""

    @staticmethod
    def get_all_requests():
        return Request.query.all()

    @staticmethod
    def get_request_by_id(request_id):
        return Request.query.get(request_id)

    @staticmethod
    def create_request(request):
        db.session.add(request)
        db.session.commit()
        return request

    @staticmethod
    def update_request(request):
        db.session.commit()
        return request

    @staticmethod
    def delete_request(request_id):
        request = Request.query.get(request_id)
        if request:
            db.session.delete(request)
            db.session.commit()
            return request
        return None

    @staticmethod
    def get_requests_filtered(data_query):
        query = Request.query
        if data_query.get("status"):
            query = query.filter(Request.status == data_query["status"])
        if data_query.get("user_id"):
            query = query.filter(Request.user_id == data_query["user_id"])
        if data_query.get("location_id"):
            query = query.filter(Request.location_id == data_query["location_id"])

        return query.all()
