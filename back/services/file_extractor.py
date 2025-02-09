"""Módulo com classes para processamento de arquivos"""

import os
from abc import ABC, abstractmethod
from services.utils import encode_image, process_response, extract_text_from_pdf
from openai import OpenAI


class FileExtractorStrategy(ABC):
    """Interface Strategy para processamento de arquivos"""

    @abstractmethod
    def process(self, file):
        """Método abstrato para processar um arquivo"""


class ImageExtractor(FileExtractorStrategy):
    """Classe de Strategy para processamento de imagens"""

    def __init__(self, client=None, prompt=None):
        if client is None:
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        if prompt is None:
            prompt = """
                    Retorne um documento JSON com os dados a seguir extraídos do documento com os respectivos nomes dos atributos:
                    1. Tipo de documento. 'tipo_de_documento'.
                    2. Nome da pessoa.  'nome'.
                    3. Data de nascimento. 'data_de_nascimento'.
                    4. Nome do pai. 'nome_do_pai'.
                    5. Nome da mãe. 'nome_da_mae'.
                    6. Naturalidade. 'naturalidade'.
                    Apenas retorne o JSON, sem qualquer outro texto.
                    """
        self.client = client
        self.prompt = prompt

    def process(self, file):
        base64_img = f"data:image/png;base64,{encode_image(file)}"
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": self.prompt},
                        {"type": "image_url", "image_url": {"url": f"{base64_img}"}},
                    ],
                }
            ],
            max_tokens=500,
        )
        return process_response(response)


class PDFExtractor(FileExtractorStrategy):
    """Classe de Strategy para processamento de PDFs"""

    def process(self, file):
        text = extract_text_from_pdf(file)
        return {"extracted_text": text}


class FileExtractorContext:
    """Contexto que usa a estratégia de processamento"""

    def __init__(self, strategy: FileExtractorStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: FileExtractorStrategy):
        """Define a estratégia de processamento"""
        self.strategy = strategy

    def process_file(self, file):
        """Processa um arquivo"""
        return self.strategy.process(file)
