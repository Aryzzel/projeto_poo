Entrega 1 (11/07 - tag: imperativa.1)
Leitura de colab sobre Git e Github e criação do projeto no Github.

Adicionar funcionalidades que permitam:

Desenhar retângulos.
Desenhar ovais.
Desenhar círculos.
Que os desenhos individuais possam ter bordas com cor.
Que os desenhos individuais tenham cor de preenchimento.

Entrega 2 (13/07 tag: OO.1)
Refatorar o sistema para seguir uma abordagem OO.
Definir uma hierarquia de classes (Figura) para contemplar os diversos tipos de desenhos: retângulos, mão livre, etc.
Adequar o programa para utilizar a hierarquia de figuras (Figura).
Adicionar desenhos de polígonos.
Separar o código em módulos (Classe Figura e subclasses em um arquivo separado, por exemplo)

Entrega 3 (16/07 tag: OO.MVC.1)
Refatorar para utilizar o padrão MVC.
Definir as classes do modelo (Figuras, Desenho, ...)
Definir uma classe ou classes para a visão
Definir uma classe ou classes para o(s) controlador(es)
Recomendação: usar a seguinte estrutura de arquivos e pastas

nome-do-projeto/
├── .git/                     # Controlado pelo Git
├── .gitignore                # Arquivos e pastas ignorados pelo Git
├── src/                      # Código-fonte principal do projeto
│   └── nome_do_projeto/      # Pacote python  
│       ├── main.py           # O programa principal
│       ├── modelo            # Classes do Model
│       │   └── ...           #
│       ├── visao             # Classes da View
│       │   └── ...
│       └── controlador       # Classes Controllers
│           └── ...

Entrega 4 (19/07 tag: OO.State.1)

Utilizar o Padrão State para evitar código condicional nos métodos do(s) controlador(es)
Adicionar as funcionalidades Salvar e Abrir
