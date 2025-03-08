# Definimos Imports como uma classe para encapsular de forma organizada e centralizada a inicialização e configuração do jogo. Ao usar uma classe, especialmente com o padrão Singleton, podemos:
# Manter estado: A classe armazena atributos (como cores, telas, assets, etc.) que persistem enquanto o jogo roda.
# Evitar inicializações repetidas: O Singleton garante que apenas uma instância seja criada e reutilizada, evitando cargas desnecessárias de recursos.
# Organizar funcionalidades: Uma classe permite agrupar métodos e atributos relacionados à configuração, facilitando o acesso e a manutenção do código, algo que uma função isolada não conseguiria fazer de forma tão estruturada.
class Imports:

    # Os duplos underlines antes e depois do nome (por exemplo, __new__ e __init__) indicam que se tratam de métodos especiais da linguagem e não são chamados diretamente pelo programador, mas automaticamente pelo Python conforme o seu funcionamento interno.

    # _instance armazena a única instância que será criada.
    _instance = None
    # _initialized garante que a inicialização (dentro de __init__) seja executada apenas uma vez.
    _initialized = False

    # O método __new__ é responsável por criar uma nova instância da classe Imports.
    # Esse método é chamado antes de __init__ para criar uma nova instância.
    def __new__(cls):
        if cls._instance is None:
            # Ele verifica se _instance é None. Se for, chama super().__new__(cls) para criar a instância e armazena em _instance.
            cls._instance = super(Imports, cls).__new__(cls)
        # Se já existir uma instância, retorna-a imediatamente, garantindo que não sejam criadas múltiplas instâncias.
        return cls._instance

    def __init__(self):
        if not self._initialized:
            # Mesmo que o construtor seja chamado várias vezes, a verificação if not self._initialized: impede que a inicialização (como carregar assets e configurações) seja repetida.
            # Após a primeira execução, _initialized é definido como True, evitando reinicializações desnecessárias.
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
            self.yellow = (255, 255, 0)

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

            # Carrega os backgrounds para diferentes gêneros
            self.menu_bg = pygame.image.load(os.path.join(self.assets_path, 'images', 'bg_menu.png'))
            self.classical_bg = pygame.image.load(os.path.join(self.assets_path, 'images', 'stage_background.png'))
            self.citypop_bg = pygame.image.load(os.path.join(self.assets_path, 'images', 'bg_citypop.png'))
            self.rock_bg = pygame.image.load(os.path.join(self.assets_path, 'images', 'bg_rock.png'))

            # Carrega as imagens de telas de término do jogo (game over e vitória)
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

            # Lista de imagens para os gatos citypop
            self.catpop_musicians = [
                pygame.image.load(os.path.join(self.assets_path, 'images', 'catpop_guitar.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'catpop_bass.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'catpop_drums.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'catpop_piano.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'catpop_dj.png')),
                pygame.image.load(os.path.join(self.assets_path, 'images', 'catpop_teclado.png'))
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

            # Dicionário com a lista de músicas disponíveis e seus nomes de arquivo, passando o gênero de cada música
            # O dicionário music_list contém os nomes das músicas como chaves e um dicionário com o nome do arquivo e o gênero da música como valores. Isso permite que o jogo saiba qual arquivo de música carregar e qual imagem de fundo exibir para cada gênero de música.
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
# O Imports é um singleton que encapsula a inicialização dos módulos do Pygame e outras configurações do jogo. Ele é responsável por carregar as imagens, definir as cores, configurar a janela do jogo e carregar as músicas disponíveis. Além disso, ele define as fontes usadas para renderizar o texto na tela. O Imports é um exemplo de encapsulamento de funcionalidades relacionadas à inicialização do jogo, tornando mais fácil acessar essas configurações em outros módulos.
# Ela garante que apenas um objeto da classe Imports seja criado e utilizado por todo o jogo.
# Com isso, ao usar a variável global "imports", o jogo sempre acessa o mesmo objeto, evitando reinicializações ou múltiplos carregamentos de módulos e assets.
# Veja como funciona: 
# new: Este método verifica se uma instância da classe já existe (usando a variável de classe _instance). Se não existir, ele cria uma nova instância e a armazena.
# init: Mesmo que o construtor seja chamado mais de uma vez, a inicialização real acontece somente na primeira vez, controlada pela flag _initialized.
imports = Imports()
