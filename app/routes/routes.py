from flask import Blueprint, request

from app.services.livros_service import criar_livro, listar_livros

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    return {"message": "API doação de livros"}

@main.route('/livros', methods=['GET'])
def get_livros():
    return listar_livros()

@main.route("/doar", methods=["POST"])
def post_livro():
    requisicao = request.get_json()

    dados = {
        'titulo': requisicao.get("titulo"),
        'categoria': requisicao.get("categoria"),
        'autor': requisicao.get("autor"),
        'image_url': requisicao.get("image_url")
    }

    return criar_livro(dados)
