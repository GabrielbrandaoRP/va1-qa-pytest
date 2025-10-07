class LivroDuplicadoException(Exception):
    pass


class LivroInvalidoException(Exception):
    pass


class Livro:
    def __init__(self, titulo: str, autor: str, paginas: int, genero: str):
        if not titulo or titulo.strip() == "":
            raise LivroInvalidoException("Título não pode ser vazio.")
        if not autor or autor.strip() == "":
            raise LivroInvalidoException("Autor não pode ser vazio.")
        if paginas <= 0:
            raise LivroInvalidoException("Número de páginas deve ser maior que zero.")
        if not genero or genero.strip() == "":
            raise LivroInvalidoException("Gênero não pode ser vazio.")

        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.genero = genero


class CatalogoLivros:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro: Livro):
        for l in self.livros:
            if l.titulo.lower() == livro.titulo.lower():
                raise LivroDuplicadoException("Livro já cadastrado.")
        self.livros.append(livro)
        return livro

    def listar_livros(self):
        return self.livros

    def buscar_por_titulo(self, titulo: str):
        for l in self.livros:
            if l.titulo.lower() == titulo.lower():
                return l
        return None

    def remover_livro(self, titulo: str):
        livro = self.buscar_por_titulo(titulo)
        if livro:
            self.livros.remove(livro)
            return True
        return False
