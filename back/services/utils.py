"""Módulo com funções utilitárias para os serviços da aplicação"""
import base64
import json
import PyPDF2

def encode_image(image):
    """Codifica uma imagem para base64"""
    return base64.b64encode(image.read()).decode('utf-8')

def extract_text_from_pdf(file):
    """Extrai texto de um arquivo PDF"""
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def process_response(response):
    """Processa a resposta da OpenAI"""
    json_string = response.choices[0].message.content
    json_string = json_string.replace("```json\n", "").replace("\n```", "")
    return json.loads(json_string)
