"""Módulo para inicializar os dados no banco de dados a partir de um arquivo JSON."""
from models import db, Location, Locker
import json


def get_data():
    """Função para carregar os dados do arquivo JSON."""
    data = None
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def initialize_data(data=None):
    """Função para inicializar os dados no banco de dados a partir de um arquivo JSON."""
    if data is None:
        # Carregar dados do arquivo JSON
        data = get_data()

    # Preenchendo a tabela de Localizações (Locations)
    for location_data in data["locations"]:
        location = Location(
            name=location_data["name"], description=location_data["description"]
        )
        db.session.add(location)
        db.session.commit()

        # Preenchendo os armários (Lockers) para cada localização
        for locker in location_data.get("lockers", []):
            locker_number = locker["number"]
            locker_status = locker["status"]

            locker = Locker(
                number=locker_number, status=locker_status, location_id=location.id
            )
            db.session.add(locker)

        # Se não houver números especificados, gerar números automaticamente
        if not location_data.get("lockers"):
            for i in range(1, location_data["capacity"] + 1):
                locker = Locker(number=i, location_id=location.id)
                db.session.add(locker)
        db.session.commit()
