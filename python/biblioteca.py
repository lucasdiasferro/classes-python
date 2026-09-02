class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        print("\n----------------------------------------------\n")
        for livro in self.livros:
            print(f"{livro.titulo} - {livro.autor}")
        print("\n----------------------------------------------\n")


livro1 = Livro("Odisséia", "Tomas Édisson")


biblioteca = Biblioteca()

biblioteca.adicionar_livro(livro1)
biblioteca.listar_livros()

livro2 = Livro("Nárnia", "Desconhecido")
livro3 = Livro("Spider-Man", "Stan-Lee")
livro4 = Livro("Sexo 1", "Anderson Silva")

biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_livro(livro4)

biblioteca.listar_livros()