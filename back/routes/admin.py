"""Rotas para a área administrativa do sistema."""

import json
from flask import render_template, Blueprint, request, redirect, url_for, jsonify
from decorators import role_required
from services.locker_request_service import LockerRequestService
from services.user_service import UserService
from services.admin_service import AdminService
from services.locker_service import LockerService
admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/availability", methods=["GET"])
@role_required("admin")
def locker_availability():
    """Rota para a disponibilidade de armários."""
    availability_data = LockerService.calculate_availability()
    
    return render_template(
        "student/availability.html", availability_data=availability_data
    )


@admin_bp.route("/users")
@role_required("admin")
def users():
    """Rota para a listagem de usuários."""

    email_filter = request.args.get("email", "")
    role_filter = request.args.get("role", "")

    data = {"email": email_filter, "role": role_filter}
    users_result = UserService.get_users_filtered(data)

    return render_template("admin/users.html", users=users_result)


@admin_bp.route("/locker-requests", methods=["GET", "POST"])
@role_required("admin")
def locker_requests():
    """Rota para visualizar as solicitações pendentes."""

    if request.method == "POST":
        status_updates = request.form.to_dict()
        LockerRequestService.process_requests(status_updates)
        return redirect(url_for("admin.locker_requests"))

    requests = LockerRequestService.get_pending_requests()
    return render_template("admin/locker_requests.html", requests=requests)

@admin_bp.route("/configure", methods=["POST", "GET"])
@role_required("admin")
def configure():
    """Rota para configurar o sistema a partir de um arquivo JSON."""
    if request.method == "POST":
        file = request.files.get("json_file")
        if file and file.filename.endswith(".json"):
            json_content = file.read().decode("utf-8")
            try:
                AdminService.process_json_file(json_content)
                return jsonify({"message": "Dados populados com sucesso!", "status": "success"})
            except (json.JSONDecodeError, ValueError) as e:
                return jsonify({"message": f"Erro ao processar o JSON: {str(e)}", "status": "error"}), 400
            except Exception as e:
                return jsonify({"message": f"Erro ao popular dados: {str(e)}", "status": "error"}), 400
    return render_template("admin/configure.html")
