from flask import jsonify

from app.repositories.livros_repository import inserir_livro, obter_livros


def listar_livros():
    dados = obter_livros()
    dados = [
        {
            "id": livro.id,
            'titulo': livro.titulo,
            'categoria': livro.categoria,
            'autor': livro.autor,
            'image_url': livro.image_url
        } for livro
        in dados
    ]
    return jsonify(dados), 200

def criar_livro(livro):
    if not livro['titulo'] or not livro['categoria'] or not livro['autor'] or not livro['image_url']:
        return "Dados insuficientes.", 400

    try:
        inserir_livro(livro['titulo'], livro['categoria'],
                      livro['autor'], livro['image_url'])
        return "Livro adicionado com sucesso.", 201
    except Exception:
        return "Erro ao adicionar livro.", 500