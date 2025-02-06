from flask import Blueprint, flash, redirect, render_template, request, url_for
from decorators import role_required
from services.user_service import UserService
from services.request_service import RequestService
from services.location_service import LocationService
from services.locker_service import LockerService
from services.reservation_service import ReservationService

student_bp = Blueprint("student", __name__)


@student_bp.route("/request-locker", methods=["GET", "POST"])
@role_required("aluno")
def request_locker():
    """Rota para o aluno solicitar um armário de uma localidade"""
    if request.method == "POST":
        location_id = request.form.get("location_id")
        if not location_id:
            flash("Por favor, selecione uma localidade.", "error")
            return redirect(url_for("student.request_locker"))
        RequestService.create_user_request(location_id)
        flash("Sua solicitação de armario foi enviada com sucesso!", "success")
        return redirect(url_for("student.request_locker"))

    locations = LocationService.get_all()
    return render_template("student/request_locker.html", locations=locations)


@student_bp.route("/my-requests", methods=["GET"])
@role_required("aluno")
def my_requests():
    """Exibe as solicitações de armários feitas pelo aluno"""
    requests = UserService.get_user_requests()
    return render_template("student/my_requests.html", requests=requests)


@student_bp.route("/my-locker", methods=["GET"])
@role_required("aluno")
def my_reservation():
    """Rota para visualizar o armário do estudante."""
    reservation = ReservationService.get_user_reservation()
    if reservation:
        return render_template("student/my_reservation.html", reservation=reservation)
    else:
        return render_template(
            "student/my_reservation.html", message="Você não tem reserva atribuída."
        )


@student_bp.route("/availability", methods=["GET"])
@role_required("aluno")
def locker_availability():
    """Rota para a disponibilidade de armários."""
    availability_data = LockerService.calculate_availability()
    return render_template(
        "student/availability.html", availability_data=availability_data
    )
