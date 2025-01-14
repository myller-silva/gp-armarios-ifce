"""Rotas para a área administrativa do sistema."""

from flask import render_template, Blueprint, request, jsonify, redirect, url_for
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


@admin_bp.route("/availability", methods=["GET"])
@role_required('admin')
def locker_availability():
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
                # "location_name": location.name,
                "location_dict": location.to_dict(),
                "total_lockers": total_lockers,
                "free_lockers": free_lockers,
                "percent_free": round(percent_free, 2),
            }
        )

    # Renderiza um template para exibir os dados
    return render_template(
        "admin/availability.html", availability_data=availability_data
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
