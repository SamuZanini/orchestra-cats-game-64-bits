class Imports:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Imports, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._initialized = True
            
            import pygame
            import time
            import random
            import os

            # Inicializa os módulos do pygame, incluindo o som
            pygame.init()
            pygame.mixer.init()

            # Definindo as cores usadas no jogo
            self.white = (255, 255, 255)
            self.black = (0, 0, 0)
            self.red = (213, 50, 80)
            self.gray = (128, 128, 128)
            self.green = (0, 255, 0)

            # Configurações da janela do jogo
            self.dis_width = 1024
            self.dis_height = 896
            self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))
            pygame.display.set_caption('Orchestra Cats')
            
            # Corrigido assets path para src/assets invés de settings/assets
            self.assets_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets')
            pygame.display.set_icon(pygame.image.load(os.path.join(self.assets_path, 'images', 'game_icon.png')))
            # Cria um objeto Clock do Pygame, que é usado para controlar a taxa de atualização (FPS) do jogo. Isso garante que o jogo rode de forma consistente em diferentes máquinas, limitando a quantidade de frames por segundo e mantendo a velocidade do jogo estável.
            self.clock = pygame.time.Clock()

            # Tamanho do "bloco" (gato) e velocidade base
            self.cat_size = 64
            self.base_speed = 5
            self.current_speed = self.base_speed

            # Carrega os arquivos de imagem a partir do diretório de assets
            # O "os" é o módulo da biblioteca padrão do Python para interações com o sistema operacional, incluindo manipulação de caminhos de arquivos. Na expressão, ele é usado para construir, de forma portátil, o caminho até a pasta "assets".
            self.cat_conductor = pygame.image.load(os.path.join(self.assets_path, 'images', 'cat_conductor.png'))
            self.cat_musician = pygame.image.load(os.path.join(self.assets_path, 'images', 'cat_violin.png'))
            self.yarn_gray = pygame.image.load(os.path.join(self.assets_path, 'images', 'yarn_gray.png'))
            self.yarn_gray_counter = pygame.image.load(os.path.join(self.assets_path, 'images', 'yarn_gray_counter.png'))
            self.yarn_red = pygame.image.load(os.path.join(self.assets_path, 'images', 'yarn_red.png'))

            # Backgrounds para diferentes gêneros
            # Carrega imagens de telas de término do jogo (game over e vitória)
            self.menu_bg = pygame.image.load(os.path.join(self.assets_path, 'images', 'bg_menu.png'))
            self.classical_bg = pygame.image.load(os.path.join(self.assets_path, 'images', 'stage_background.png'))
            self.citypop_bg = pygame.image.load(os.path.join(self.assets_path, 'images', 'bg_citypop.png'))
            self.rock_bg = pygame.image.load(os.path.join(self.assets_path, 'images', 'bg_rock.png'))

            # Carrega imagens de telas de término
            self.game_over_img = pygame.image.load(os.path.join(self.assets_path, 'images', 'game_over.png'))
            self.you_win_img = pygame.image.load(os.path.join(self.assets_path, 'images', 'you_win.png'))

            # Lista de imagens para os gatos músicos clássicos
            self.cat_musicians = [
                pygame.image.load(os.path.join(self.assets_path, 'images', 'cat_violin.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'cat_trompete.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'cat_cello.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'cat_piano.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'cat_trombone.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'cat_trompa.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'cat_clarinete.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'cat_saxofone.png'))
            ]

            # Lista de imagens para os gatos pop
            self.catpop_musicians = [
                pygame.image.load(os.path.join(self.assets_path, 'images', 'catpop_guitar.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'catpop_bass.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'catpop_drums.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'catpop_piano.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'catpop_dj.png'))
            ]
            self.catpop_conductor = pygame.image.load(os.path.join(self.assets_path, 'images', 'catpop_vocal.png'))

            # Lista de imagens para os gatos rock
            self.catrock_musicians = [
                pygame.image.load(os.path.join(self.assets_path, 'images', 'catrock_guitar.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'catrock_piano.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'catrock_drums.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'catrock_dj.png'))
            ]
            self.catrock_conductor = pygame.image.load(os.path.join(self.assets_path, 'images', 'catrock_vocal.png'))

            # Dicionário com a lista de músicas disponíveis e seus nomes de arquivo
            self.music_list = {
                "Paganini - Caprice 24": {"file": "caprice24.MP3", "genre": "classical"},
                "Paganini - La Capanella": {"file": "laCampanella.MP3", "genre": "classical"},
                "Chopin - Nocturne op.9 No.2": {"file": "nocturne.mp3", "genre": "classical"},
                "Chopin - Nocturne in C Sharp Minor for Violin and Piano": {"file": "nocturneViolin.MP3", "genre": "classical"},
                "Oskar Rieding - Violin Concerto in B Minor, Op. 35: I. Allegro moderato": {"file": "rieding.MP3", "genre": "classical"},
                "Vivaldi - The Four Seasons, 'Winter'": {"file": "winter.mp3", "genre": "classical"},
                "Miki Matsubara - Stay With Me": {"file": "stayWithMe.mp3", "genre": "citypop"},
                "Likin Park - By Myself": {"file": "byMyself.mp3", "genre": "rock"},
                "Linki Park - One More Light": {"file": "oneMoreLight.mp3", "genre": "rock"},
                "Linki Park - Numb": {"file": "numb.MP3", "genre": "rock"},
                "Linkin Park - Somewhere I Belong": {"file": "somewhereIBelong.MP3", "genre": "rock"}
            }

            # Define as fontes usadas para exibição de texto, com suporte a emoji
            self.font_style = pygame.font.SysFont("Segoe UI Emoji", 25) # Alterado: fonte com suporte a emoji
            self.score_font = pygame.font.SysFont("Segoe UI Emoji", 35) # Alterado: fonte com suporte a emoji
            
            # Faz os módulos do pygame facilmente acessíveis
            self.pygame = pygame
            self.time = time
            self.random = random
            self.os = os

# Cria uma single instance que vai ser usada durante o game
imports = Imports()
