from src.settings.imports.imports import imports
from src.settings.display.menu import show_menu, show_end_screen

def draw_grid():
    for i in range(0, imports.dis_width, imports.cat_size):
        imports.pygame.draw.line(imports.dis, (128, 128, 128), (i, 0), (i, imports.dis_height))
    for i in range(0, imports.dis_height, imports.cat_size):
        imports.pygame.draw.line(imports.dis, (128, 128, 128), (0, i), (imports.dis_width, i))

def our_cats(cat_size, cat_list, cat_types, current_conductor, current_musicians):
    # Exibe os gatos na tela.
    # A última posição da lista representa a cabeça (o condutor)
    # E os demais, o corpo representado por diferentes tipos de gatos músicos.
    if not cat_list:
        return
    
    # No início do loop de jogo (na função gameLoop), "cat_types" é inicializado como uma lista vazia. Quando o gato (cobrinha) come a comida, o código adiciona um novo elemento a "cat_types" usando:
    # cat_types.append(random.choice(cat_musicians))
    # Assim, cada vez que a cobra cresce, um novo elemento (uma imagem escolhida aleatoriamente da lista "cat_musicians") é adicionado ao array "cat_types".
    # Na função our_cats: O laço que desenha os gatos percorre "cat_list" (as posições dos segmentos da cobra). Para o último segmento (a cabeça), ele desenha a imagem "cat_conductor". Para os demais segmentos (corpo), ele utiliza as imagens armazenadas em "cat_types", acessando-as pelo índice "i". Isso faz com que o corpo da cobra seja desenhado com imagens dos músicos, conforme foram adicionadas à lista em "cat_types".
    # A confusão aqui ocorre devido a ordem de declaração. gameLoop virá após essa função.
    for i, pos in enumerate(cat_list):
        if i == len(cat_list) - 1:  # Último elemento: cabeça, usa a imagem do condutor
            imports.dis.blit(current_conductor, (pos[0], pos[1]))
        elif i < len(cat_types):  # Elementos do corpo usam imagens dos músicos
            imports.dis.blit(current_musicians[i % len(current_musicians)], (pos[0], pos[1]))

# Define quanto os gatos crescem a cada refeição
incremento_gatos = 1

def gameLoop():
    # Função principal onde o jogo roda.
    # Executa o menu de seleção de música, o loop do jogo, controle de colisões,
    # incremento do tamanho da "cobra" e verificação de término.
    while True:
        # Chama a função show_menu(), que exibe o menu para o jogador escolher uma música. Essa função retorna o nome da música selecionada (ou None se o menu for fechado). Assim, o valor retornado por show_menu() é atribuído à variável selected_music para que o jogo saiba qual música tocar. Se selected_music for false (ou seja, se o jogador fechar o menu sem escolher), o código executa return, encerrando o jogo.
        # Em resumo, exibe o menu e obtém a música selecionada. Se o menu for fechado, encerra.
        selected_music = show_menu()
        if not selected_music:
            return
        
        # Determina o gênero da música e define os sprites e background apropriados
        music_genre = imports.music_list[selected_music]["genre"]
        if music_genre == "classical":
            current_bg = imports.classical_bg
            current_conductor = imports.cat_conductor
            current_musicians = imports.cat_musicians
        elif music_genre == "citypop":
            current_bg = imports.citypop_bg
            current_conductor = imports.catpop_conductor
            current_musicians = imports.catpop_musicians
        elif music_genre == "rock":
            current_bg = imports.rock_bg
            current_conductor = imports.catrock_conductor
            current_musicians = imports.catrock_musicians
        
        # Carrega e reproduz a música selecionada
        imports.pygame.mixer.music.load(imports.os.path.join(imports.assets_path, 'music', imports.music_list[selected_music]["file"]))
        imports.pygame.mixer.music.play()
        
        # Nenhuma das instância abaixo foi atingida pelo jogador ainda, portanto são inicializadas como False.
        game_over = False
        won = False
        
        # Define a posição inicial da cabeça (gato condutor) no centro da tela.
        x1 = imports.dis_width / 2
        y1 = imports.dis_height / 2

        # Inicializa a mudança de posição para mover de um bloco de cada vez
        # Essas duas linhas definem o deslocamento inicial da posição da cabeça (x1 e y1) para cada atualização do jogo, ou seja, a "passada" que o gato (cabeça da cobra) dá a cada movimento.
        # x1_change = cat_size: Isso significa que, por padrão, a posição horizontal (x1) será atualizada em passos iguais ao tamanho do bloco (cat_size, que é 64 pixels). Ou seja, a cada movimento, a cabeça se desloca 64 pixels para a direita.
        # y1_change = 0: Aqui, a mudança na posição vertical (y1) é 0, ou seja, não há deslocamento vertical no movimento inicial.
        # Em resumo, essas linhas configuram o movimento inicial para que o gato se mova discretamente, de um "bloco" para outro da grade, inicialmente se deslocando apenas na horizontal (para a direita).
        x1_change = imports.cat_size  
        y1_change = 0
        
        # Lista que guarda todas as posições dos gatos e lista para imagens dos músicos
        # Essa variável é uma lista de posições onde cada elemento representa um segmento da cobra. Como o jogo está começando, a cobra possui apenas a cabeça. Assim, a lista inicia com um único elemento, que é uma lista contendo as coordenadas iniciais (x1, y1) da cabeça – que foi definida para estar no centro da tela.
        cat_list = [[x1, y1]]
        # Essa lista vai armazenar as imagens para os segmentos do corpo da cobra (os gatos músicos). Cada vez que a cobra come a comida, é adicionada uma nova imagem escolhida aleatoriamente de cat_musicians. No início do jogo, como a cobra tem apenas a cabeça, não há corpo, por isso essa lista inicia vazia.
        cat_types = []
        # Essa variável representa o tamanho (ou a quantidade de segmentos) da cobra. Como a cobra começa com apenas a cabeça, seu comprimento inicial é 1.
        length_of_cats = 1
        current_speed = imports.base_speed
        boost_end_time = 0 # Tempo final do boost, se houver (0 indica sem boost)
        
        # Posiciona a "comida" (linha de novelo) em posição aleatória
        # Essa linha posiciona a "comida" (o novelo) de forma aleatória, mas alinhada a uma grade definida pelo tamanho do bloco (cat_size). Vamos quebrá-la em partes:
        # random.randrange(0, dis_width - cat_size): Gera um número inteiro aleatório entre 0 e (dis_width - cat_size). Isso garante que a comida não seja gerada fora da tela, já que a largura da imagem (cat_size) é considerada.
        # Divisão por cat_size e round(): O número aleatório é dividido por cat_size e, em seguida, arredondado. Isso transforma o número em uma unidade de "blocos". Por exemplo, se cat_size é 64, dividindo e arredondando você obtém um número inteiro representando a coluna da grade.
        # Multiplicação por cat_size: Multiplicando esse número arredondado por cat_size, você converte novamente de "bloco" para pixels. Assim, o valor final será múltiplo de cat_size, garantindo que a comida esteja alinhada à grade do jogo.
        # Em resumo, esse código seleciona uma posição horizontal aleatória na tela, mas garantindo que a comida esteja "encaixada" em um dos blocos de tamanho cat_size. O mesmo acontece com a coordenada vertical (foody), para que a comida fique posicionada corretamente na grade.
        foodx = round(imports.random.randrange(0, imports.dis_width - imports.cat_size) / imports.cat_size) * imports.cat_size
        foody = round(imports.random.randrange(0, imports.dis_height - imports.cat_size) / imports.cat_size) * imports.cat_size

        # Define aleatoriamente se o novelo é vermelho (que ativa boost)
        is_red_yarn = imports.random.random() < 0.2

        while not game_over:
            # Verifica os eventos (fechar, teclas pressionadas)
            for event in imports.pygame.event.get():
                if event.type == imports.pygame.QUIT:
                    game_over = True
                elif event.type == imports.pygame.KEYDOWN:
                    if len(cat_list) > 1:
                        if (event.key == imports.pygame.K_LEFT and pygameKey == imports.pygame.K_RIGHT) or (event.key == imports.pygame.K_RIGHT and pygameKey == imports.pygame.K_LEFT) or(event.key == imports.pygame.K_UP and pygameKey == imports.pygame.K_DOWN) or (event.key == imports.pygame.K_DOWN and pygameKey == imports.pygame.K_UP):
                            continue
                    pygameKey = event.key
                    if event.key == imports.pygame.K_LEFT:
                        x1_change = -imports.cat_size
                        y1_change = 0
                    elif event.key == imports.pygame.K_RIGHT:
                        x1_change = imports.cat_size
                        y1_change = 0
                    elif event.key == imports.pygame.K_UP:
                        # No Pygame (e na maioria dos sistemas de coordenadas em gráficos), a origem (0, 0) fica no canto superior esquerdo da tela, e o eixo Y aumenta para baixo. Por isso, para mover o objeto para cima, é necessário diminuir o valor de Y (ou seja, subtrair), resultando em -cat_size.
                        y1_change = -imports.cat_size
                        x1_change = 0
                    elif event.key == imports.pygame.K_DOWN:
                        y1_change = imports.cat_size
                        x1_change = 0

            # Atualiza a posição da cabeça do gato conforme a direção
            x1 += x1_change
            y1 += y1_change

            # Verifica se a cabeça bateu na borda da tela
            if x1 >= imports.dis_width or x1 < 0 or y1 >= imports.dis_height or y1 < 0:
                game_over = True
                won = False
                imports.pygame.mixer.music.stop()
                break
            
            draw_grid()
            # Usa o background apropriado para o gênero atual
            imports.dis.blit(current_bg, (0, 0))
            draw_grid()
            
            # Desenha o "novelo" (comida): cor vermelha ou cinza conforme o estado
            if is_red_yarn:
                imports.dis.blit(imports.yarn_red, (foodx, foody))
            else:
                imports.dis.blit(imports.yarn_gray, (foodx, foody))

            # Atualiza a posição da cabeça do gato e faz se movimentar na tela de acordo com x1 e y1 passados acima  
            cat_head = [x1, y1]
            
            # Verifica colisão contra o corpo (self-collision)
            # A sintaxe [:-1] em Python é usada para fatiamento (slicing) de listas e significa "todos os elementos, exceto o último". No contexto do código: isso verifica se a posição atual da cabeça (cat_head) está em todas as posições armazenadas em cat_list menos a última. Geralmente, essa expressão é usada para detectar uma colisão da cabeça com o corpo da cobra (pois o último elemento representa a cabeça, e não queremos compará-la consigo mesma).
            if cat_head in cat_list[:-1]:
                game_over = True
                won = False
                imports.pygame.mixer.music.stop()
                break
            
            # Adiciona a nova posição da cabeça à lista
            cat_list.append(cat_head)
            
            # Remove a posição mais antiga se a cobra já atingiu o tamanho necessário
            if len(cat_list) > length_of_cats:
                del cat_list[0]
                if cat_types and len(cat_types) > length_of_cats - 1:
                    # Primeiro, verifica se cat_types não está vazia.
                    # Em seguida, checa se o número de elementos em cat_types é maior do que length_of_cats - 1.
                    # Como length_of_cats representa o tamanho total da cobra (inclusive a cabeça) e cat_types guarda somente as imagens do corpo (excluindo a cabeça), o número ideal de elementos em cat_types é exatamente length_of_cats - 1.
                    # Se a condição acima for verdadeira, a primeira imagem (índice 0) é removida da lista.
                    # Essa remoção sincroniza o tamanho da lista de corpo com o comprimento atual da cobra, garantindo que ela não acumule imagens antigas que não correspondem mais aos segmentos exibidos.
                    del cat_types[0]
            
            # Passa os sprites atuais para a função our_cats
            our_cats(imports.cat_size, cat_list, cat_types, current_conductor, current_musicians)
            
            # Exibe o contador de pontos (tamanho da cobra) utilizando um novelo cinza como ícone
            imports.dis.blit(imports.yarn_gray_counter, (10, 10))
            score = imports.score_font.render(str(length_of_cats), True, imports.white)
            # Desenha (renderiza) a superfície de texto contida em score na tela. O posicionamento é calculado da seguinte forma: O valor do eixo X é dado por 10 + yarn_gray_counter.get_width() + 5, o que significa que o texto será desenhado a 10 pixels da margem esquerda, mais o tamanho (largura) da imagem yarn_gray_counter e mais um adicional de 5 pixels para espaçamento. Isso posiciona o texto imediatamente à direita da imagem do contador (novelo cinza). O eixo Y é definido como 10, posicionando o texto a 10 pixels do topo da tela.
            # Em resumo, essa linha exibe o score (pontos/ tamanho da cobra) alinhado ao lado da imagem do contador que é desenhada anteriormente no canto superior esquerdo da tela.
            imports.dis.blit(score, (10 + imports.yarn_gray_counter.get_width() + 5, 10))
            
            imports.pygame.display.update()
            
            # Verifica colisão da cabeça com a comida usando retângulos para colisão
            head_rect = imports.pygame.Rect(x1, y1, imports.cat_size, imports.cat_size)
            food_rect = imports.pygame.Rect(foodx, foody, imports.cat_size, imports.cat_size)
            if head_rect.colliderect(food_rect):
                # Reposiciona a comida
                foodx = round(imports.random.randrange(0, imports.dis_width - imports.cat_size) / imports.cat_size) * imports.cat_size
                foody = round(imports.random.randrange(0, imports.dis_height - imports.cat_size) / imports.cat_size) * imports.cat_size
                
                # Aumenta o tamanho da cobra
                length_of_cats += incremento_gatos
                # Usa os músicos apropriados para o gênero atual
                cat_types.append(1)  # Apenas para manter o controle do comprimento
                
                # Se a comida era vermelha, aplica uma aceleração temporária (boost)
                if is_red_yarn:
                    current_speed = imports.base_speed + 2
                    boost_end_time = imports.time.time() + 3 # Boost dura 3 segundos
                    is_red_yarn = False
                else:
                    # Possibilidade de a próxima comida ser vermelha
                    is_red_yarn = imports.random.random() < 0.2

            # Verifica se o tempo do boost expirou; se sim, retorna a velocidade normal
            if boost_end_time and imports.time.time() > boost_end_time:
                current_speed = imports.base_speed
                boost_end_time = 0

            # Atualiza a tela e controla a velocidade do jogo
            imports.clock.tick(current_speed)
            
            # Se a música terminou, assume vitória e encerra o loop de jogo
            if not imports.pygame.mixer.music.get_busy():
                game_over = True
                won = True
                break
        
        # Exibe a tela de término e verifica se o usuário deseja jogar novamente
        if not show_end_screen(won):
            break

    imports.pygame.quit()
    quit()

# Inicia o jogo chamando o loop principal
gameLoop()
