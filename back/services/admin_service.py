import json
from data_initializer import initialize_data


class AdminService:
    """Classe de serviço para a área administrativa."""

    @staticmethod
    def process_json_file(json_content: str):
        """Processa o JSON para inicializar dados."""
        try:
            data = json.loads(json_content)
            initialize_data(data)
            return "Dados populados com sucesso!"
        except json.JSONDecodeError as e:
            raise ValueError(f"Erro ao processar o JSON: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"Erro ao popular dados: {str(e)}")
