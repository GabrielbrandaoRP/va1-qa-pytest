 ### CRUD de Livros - Avaliação Unidade 1
 ## Aluno: Gabriel Roberto Pinheiro Brandão



 Descrição
Aplicação simples em Python para gerenciar um catálogo de livros  
O foco do projeto é testar as regras de negócio com os testes unitários automatizados (Pytest)
![Pytest](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmgARH8RZDgTTzPZEtj1I1xI3Yk9r84EUNdw&s)


 Regras de Negócio Testadas
1. O título do livro não pode ser vazio 
2. A nota do livro deve estar entre 0 e 10 
3. O gênero não pode ser vazio  
4. Não é permitido cadastrar livros duplicados(mesmo título, independente de maiúsculas/minúsculas).  
5. Deve ser possível buscar livros pelo título  
6. Deve ser possível remover livros do catálogo  
7. Tentar remover um livro inexistente deve retornar False

**Como testar**
Dentro da pasta *tests* execute o seguinte comando
 no terminal executar: `pytest test_livros.py` 

 


