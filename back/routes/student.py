from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask import session
from decorators import role_required
from models import Reservation, Request, Location
from models import db


student_bp = Blueprint("student", __name__)

@student_bp.route("/request-locker", methods=["GET", "POST"])
@role_required('aluno')
def request_locker():
    """Rota para o aluno solicitar um armário de uma localidade"""
    if request.method == "POST":
        location_id = request.form.get("location_id")
        
        if not location_id:
            flash("Por favor, selecione uma localidade.", "error")
            return redirect(url_for("student.request_locker"))
        user = session.get("user")
        # Criação da solicitação no banco de dados
        new_request = Request(
            user_id=user["id"],
            location_id=location_id,
        )
        db.session.add(new_request)
        db.session.commit()
        flash("Sua solicitação foi enviada com sucesso!", "success")
        return redirect(url_for("student.request_locker"))
    
    # Obter todas as localidades disponíveis
    locations = Location.query.all()
    return render_template("student/request_locker.html", locations=locations)

# @student_bp.route("/requests")
# @role_required('aluno')
# def requests():
#     """Rota para listar as solicitações de reserva do aluno"""
#     reservations = Reservation.query.filter_by(user_id=1).all()
#     return render_template("student/requests.html", reservations=reservations)

from flask import jsonify
@student_bp.route("/my-requests", methods=["GET"])
@role_required('aluno')
def my_requests():
    """Exibe as solicitações de armários feitas pelo aluno"""
    user = session.get("user")
    user_id = user["id"]
    requests = Request.query.filter_by(user_id=user_id).all()
    # return jsonify([request.to_dict() for request in requests])
    return render_template("student/my_requests.html", requests=requests)


@student_bp.route("/locker")
@role_required('aluno')
def locker():
    """Rota para listar os armários do aluno"""
    return render_template("student/locker.html")