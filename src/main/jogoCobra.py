import os
import sys

# Adiciona o diretório raiz do projeto ao path do sistema para que seja possível importar os módulos do jogo
project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, project_root)

# Importa as funções necessárias para rodar o jogo
from src.settings.imports.imports import imports
from src.settings.display.menu import show_menu
from src.settings.display.menu import show_end_screen
from src.settings.commands.gameLoop import our_cats, gameLoop

# Em Python, um módulo é simplesmente um arquivo que contém código Python (funções, classes, variáveis, etc.) e que pode ser importado e reutilizado em outros scripts ou módulos. Essa abordagem incentiva a organização e a reutilização do código, permitindo que funcionalidades sejam separadas em arquivos distintos e facilmente integradas ao seu projeto.
# Em Python, cada módulo possui uma variável especial chamada __name__.
# Se o módulo está sendo executado diretamente (por exemplo, através do comando python jogoCobra.py), o valor de __name__ é "__main__".
# Essa checagem permite que o bloco seja executado apenas quando o módulo é a entrada principal do programa, e não quando ele é importado por outro módulo.
# Dentro do bloco condicional, é chamada a função gameLoop(), que é responsável por iniciar a execução do jogo.
# Essa função contém a lógica principal do jogo, mantendo a execução e atualizando o estado conforme necessário.
# Portanto, quando você executa jogoCobra.py diretamente, o bloco dentro do if é ativado e o jogo inicia a sua execução através da chamada de gameLoop().
if __name__ == "__main__":
    gameLoop()
