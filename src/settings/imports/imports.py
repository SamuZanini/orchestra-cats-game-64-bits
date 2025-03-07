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
            
            # Fix assets path to point to src/assets instead of settings/assets
            self.assets_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets')
            pygame.display.set_icon(pygame.image.load(os.path.join(self.assets_path, 'images', 'game_icon.png')))
            
            self.clock = pygame.time.Clock()

            # Tamanho do "bloco" (gato) e velocidade base
            self.cat_size = 64
            self.base_speed = 5
            self.current_speed = self.base_speed

            # Carrega os arquivos de imagem
            self.cat_conductor = pygame.image.load(os.path.join(self.assets_path, 'images', 'cat_conductor.png'))
            self.cat_musician = pygame.image.load(os.path.join(self.assets_path, 'images', 'cat_violin.png'))
            self.yarn_gray = pygame.image.load(os.path.join(self.assets_path, 'images', 'yarn_gray.png'))
            self.yarn_gray_counter = pygame.image.load(os.path.join(self.assets_path, 'images', 'yarn_gray_counter.png'))
            self.yarn_red = pygame.image.load(os.path.join(self.assets_path, 'images', 'yarn_red.png'))
            self.stage_bg = pygame.image.load(os.path.join(self.assets_path, 'images', 'stage_background.png'))

            # Carrega imagens de telas de término
            self.game_over_img = pygame.image.load(os.path.join(self.assets_path, 'images', 'game_over.png'))
            self.you_win_img = pygame.image.load(os.path.join(self.assets_path, 'images', 'you_win.png'))

            # Lista de imagens para os gatos músicos
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

            # Lista de músicas disponíveis
            self.music_list = {
                "Paganini - Caprice 24": "caprice24.MP3",
                "Paganini - La Capanella": "laCampanella.MP3",
                "Chopin - Nocturne op.9 No.2": "nocturne.mp3",
                "Chopin - Nocturne in C Sharp Minor for Violin and Piano": "nocturneViolin.MP3",
                "Oskar Rieding - Violin Concerto in B Minor, Op. 35: I. Allegro moderato": "rieding.MP3",
                "Vivaldi - The Four Seasons, 'Winter'": "winter.mp3",
                "Miki Matsubara - Stay With Me": "stayWithMe.mp3",
                "Likin Park - By Myself": "byMyself.mp3",
                "Linki Park - One More Light": "oneMoreLight.mp3",
                "Linki Park - Numb": "numb.MP3",
                "Linkin Park - Somewhere I Belong": "somewhereIBelong.MP3"
            }

            # Define as fontes
            self.font_style = pygame.font.SysFont("Segoe UI Emoji", 25)
            self.score_font = pygame.font.SysFont("Segoe UI Emoji", 35)
            
            # Make pygame modules easily accessible
            self.pygame = pygame
            self.time = time
            self.random = random
            self.os = os

# Create a single instance that will be used throughout the game
imports = Imports()
