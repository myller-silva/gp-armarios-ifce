"""Rotas para processamento de arquivos enviados pelo usuário"""

from flask import Blueprint, request, jsonify, render_template
from services.file_extractor import (
    FileExtractorContext,
    ImageExtractor,
    PDFExtractor,
)

files_bp = Blueprint("files", __name__)


@files_bp.route("/extract_from_file", methods=["POST", "GET"])
def extract_from_file():
    """Rota para processar um arquivo enviado pelo usuário"""
    if request.method == "GET":
        return render_template(
            "upload.html",
            title="Extrair Dados de Arquivo",
            action="/files/extract_from_file",
        )

    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    filename = file.filename

    if filename.lower().endswith(("png", "jpg", "jpeg")):
        processor = FileExtractorContext(ImageExtractor())
    elif filename.lower().endswith("pdf"):
        processor = FileExtractorContext(PDFExtractor())
    else:
        return jsonify({"error": "Unsupported file type"}), 400

    try:
        data = processor.process_file(file)
        return render_template("result_json.html", data=data)
    except Exception as e:
        return render_template("error.html", code=500, message=str(e)), 500
