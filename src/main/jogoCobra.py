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

if __name__ == "__main__":
    gameLoop()
