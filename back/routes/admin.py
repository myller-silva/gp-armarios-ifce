"""Rotas para a área administrativa do sistema."""

from flask import render_template, Blueprint, request, redirect, url_for
from models import Location, User
import json
from data_initializer import initialize_data
from decorators import role_required

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/configure", methods=["GET", "POST"])
@role_required('admin')
def configure():
    if request.method == "POST":
        file = request.files.get("json_file")
        if file and file.filename.endswith(".json"):
            json_data = file.read().decode("utf-8")
            try:
                data = json.loads(json_data)
                initialize_data(data)
                return "Dados populados com sucesso!"
            except json.JSONDecodeError as e:
                return f"Erro ao processar o JSON: {str(e)}"
            except Exception as e:
                return f"Erro ao popular dados: {str(e)}"
    return render_template("admin/configure.html")


@admin_bp.route("/populate")
@role_required('admin')
def populate():
    try:
        json_file = request.args.get("json_file")
        with open(json_file, "r") as f:
            json_data = f.read()
            initialize_data(json_data)
        return "Dados populados com sucesso!"
    except Exception as e:
        return f"Erro ao popular dados: {e}"

from services.locker_availability_service import calculate_availability

@admin_bp.route("/availability", methods=["GET"])
@role_required('admin')
def locker_availability():
    """Rota para a disponibilidade de armários."""
    locker_availability = calculate_availability()

    return render_template(
        "admin/availability.html", availability_data=locker_availability
    )


@admin_bp.route("/users")
@role_required('admin')
def users():
    """Rota para a listagem de usuários."""
    # Captura os parâmetros de filtro da URL
    email_filter = request.args.get("email", "")
    role_filter = request.args.get("role", "")

    # Inicia a consulta de usuários
    query = User.query

    # Aplica os filtros
    if email_filter:
        query = query.filter(User.email.ilike(f"%{email_filter}%"))
    if role_filter:
        query = query.filter(User.role == role_filter)

    # Executa a consulta
    users = query.all()

    # Passa os usuários filtrados para o template
    return render_template("admin/users.html", users=users)


from services.locker_request_service import LockerRequestService
@admin_bp.route('/locker-requests', methods=["GET", "POST"])
@role_required('admin')
def locker_requests():
    """Rota para visualizar as solicitações pendentes."""
    if request.method == "POST":
        # Processa as alterações de status através do serviço
        status_updates = request.form.to_dict()  # Converte o formulário para um dicionário
        LockerRequestService.process_requests(status_updates)
        
        return redirect(url_for('admin.locker_requests'))  
    # # Consulta todas as solicitações pendentes
    # requests = Request.query.filter_by(status='pendente').all()
    requests = LockerRequestService.get_pending_requests()
    return render_template("admin/locker_requests.html", requests=requests)

