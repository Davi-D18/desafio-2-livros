
from app.extensions import db
from app.models.livros import Livros


def obter_livros():
    return Livros.query.all()


def inserir_livro(titulo, categoria, autor, image_url):
    livros = Livros(titulo=titulo, categoria=categoria, autor=autor, image_url=image_url)
    db.session.add(livros)
    db.session.commit()
    return Livros

