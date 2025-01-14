from models import Location

def calculate_availability():
    """
    Calcula a disponibilidade de armários para todas as localizações (blocos).

    Returns:
        list: Lista de dicionários contendo os dados de disponibilidade de cada localização.
    """
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
                "location_dict": location.to_dict(),
                "total_lockers": total_lockers,
                "free_lockers": free_lockers,
                "percent_free": round(percent_free, 2),
            }
        )

    return availability_data
