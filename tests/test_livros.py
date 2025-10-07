import sys
import os
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from livros import (
    Livro,
    CatalogoLivros,
    LivroDuplicadoException,
    LivroInvalidoException
)


def test_criar_livro_valido():
    livro = Livro("O Hobbit", "J.R.R. Tolkien", 310, "Fantasia")
    assert livro.titulo == "O Hobbit"
    assert livro.autor == "J.R.R. Tolkien"
    assert livro.paginas == 310
    assert livro.genero == "Fantasia"


def test_nao_deve_permitir_titulo_vazio():
    with pytest.raises(LivroInvalidoException):
        Livro("", "George Orwell", 300, "Distopia")


def test_nao_deve_permitir_autor_vazio():
    with pytest.raises(LivroInvalidoException):
        Livro("1984", "", 300, "Distopia")


def test_nao_deve_permitir_paginas_menor_ou_igual_a_zero():
    with pytest.raises(LivroInvalidoException):
        Livro("Dom Casmurro", "Machado de Assis", 0, "Romance")


def test_nao_deve_permitir_genero_vazio():
    with pytest.raises(LivroInvalidoException):
        Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 96, "")


def test_deve_adicionar_livro_no_catalogo():
    catalogo = CatalogoLivros()
    livro = Livro("O Hobbit", "J.R.R. Tolkien", 310, "Fantasia")
    catalogo.adicionar_livro(livro)
    assert len(catalogo.listar_livros()) == 1


def test_nao_deve_permitir_livro_duplicado():
    catalogo = CatalogoLivros()
    l1 = Livro("O Hobbit", "J.R.R. Tolkien", 310, "Fantasia")
    l2 = Livro("o hobbit", "Outro Autor", 200, "Aventura")
    catalogo.adicionar_livro(l1)
    with pytest.raises(LivroDuplicadoException):
        catalogo.adicionar_livro(l2)


def test_deve_buscar_livro_por_titulo():
    catalogo = CatalogoLivros()
    livro = Livro("1984", "George Orwell", 328, "Distopia")
    catalogo.adicionar_livro(livro)
    resultado = catalogo.buscar_por_titulo("1984")
    assert resultado.autor == "George Orwell"
    assert resultado.paginas == 328


def test_buscar_livro_inexistente_retorna_none():
    catalogo = CatalogoLivros()
    resultado = catalogo.buscar_por_titulo("LivroQueNaoExiste")
    assert resultado is None


def test_deve_remover_livro():
    catalogo = CatalogoLivros()
    livro = Livro("O Hobbit", "J.R.R. Tolkien", 310, "Fantasia")
    catalogo.adicionar_livro(livro)
    assert catalogo.remover_livro("O Hobbit") is True
    assert len(catalogo.listar_livros()) == 0


def test_remover_livro_inexistente_retorna_false():
    catalogo = CatalogoLivros()
    assert catalogo.remover_livro("LivroQueNaoExiste") is False
