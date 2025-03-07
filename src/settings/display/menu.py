from src.settings.imports.imports import imports

def show_menu():
    # Exibe o menu principal, permitindo a escolha da música.
    # O usuário pode navegar com as setas e confirmar com ENTER.

    # Define o índice do item atualmente selecionado, inicialmente o primeiro item do menu.
    selected = 0
    # Cria uma lista com todos os nomes das músicas disponíveis, extraídos das chaves do dicionário music_list.
    menu_items = list(imports.music_list.keys())
    
    # A função entra em um loop infinito (while True:) para manter o menu ativo até que o usuário faça uma escolha ou feche a janela.
    while True:
        # Preenche a tela com a cor preta, basicamente limpando a tela a cada iteração.
        imports.dis.fill(imports.black)
        # Desenha a imagem de fundo (stage_bg) na posição (0, 0).
        imports.dis.blit(imports.stage_bg, (0, 0))
        
        # Renderiza o título centralizado
        # O título "Orchestra Cats 🐈‍" é renderizado usando a fonte score_font e depois centralizado horizontalmente, calculando a posição com (dis_width - title.get_width()) / 2 e posicionado na vertical em 50 pixels.
        title = imports.score_font.render("Orchestra Cats 🐈‍", True, imports.white)
        imports.dis.blit(title, [ (imports.dis_width - title.get_width()) / 2, 50 ])
        
        # Renderiza cada item do menu e destaca o selecionado
        for i, item in enumerate(menu_items):
            color = imports.red if i == selected else imports.white
            text = imports.font_style.render(item, True, color)
            # Alterado: itens do menu centralizados horizontalmente
            # Utiliza dis.blit() para desenhar o texto de cada item centralizado horizontalmente e posicionado verticalmente com um espaçamento de 50 pixels (a posição vertical é calculada como 150 + i*50).
            imports.dis.blit(text, [ (imports.dis_width - text.get_width()) / 2, 150 + i*50 ])
        
        # Atualiza a tela para mostrar as mudanças feitas (fundo, título e itens do menu).
        imports.pygame.display.update()
        
        # Lida com os eventos de teclado e fechamento da janela
        for event in imports.pygame.event.get():
            # Se o evento é imports.pygame.QUIT, ou seja, se o jogador fechar a janela, a função retorna None para indicar que não houve seleção de música.
            if event.type == imports.pygame.QUIT:
                return None
            
            # Se o evento for do tipo imports.pygame.KEYDOWN (tecla pressionada)
            if event.type == imports.pygame.KEYDOWN:
                if event.key == imports.pygame.K_UP:
                    # Se a tecla pressionada for a seta para cima (imports.pygame.K_UP): o índice selecionado é decrementado. A expressão (selected - 1) % len(menu_items) garante que, se o índice ficar negativo, ele seja ajustado para o último item, criando uma navegação circular.
                    selected = (selected - 1) % len(menu_items)
                elif event.key == imports.pygame.K_DOWN:
                    # Se a tecla pressionada for a seta para baixo (imports.pygame.K_DOWN): o índice selecionado é incrementado, utilizando também a operação módulo para navegar de forma circular.
                    selected = (selected + 1) % len(menu_items)
                elif event.key == imports.pygame.K_RETURN:
                    # Se a tecla pressionada for ENTER (imports.pygame.K_RETURN): o item atualmente selecionado (a música correspondente) é retornado e o menu é encerrado.
                    return menu_items[selected]
                
def show_end_screen(won=False):
    # Exibe a tela de término (vitória ou derrota) e aguarda o comando do usuário para reiniciar.
    # Retorna True se o usuário deseja jogar novamente, False caso contrário.
    waiting = True
    while waiting:
        imports.dis.fill(imports.black)
        if won:
            # O cálculo (dis_width/2 - imports.you_win_img.get_width()/2) centraliza horizontalmente a imagem: ele pega a metade da largura da tela e subtrai metade da largura da imagem, fazendo com que sua posição X seja justamente no meio. De forma similar, (dis_height/2 - imports.you_win_img.get_height()/2) centraliza verticalmente a imagem.
            imports.dis.blit(imports.you_win_img, (imports.dis_width/2 - imports.you_win_img.get_width()/2, imports.dis_height/2 - imports.you_win_img.get_height()/2))
            text = imports.font_style.render("Pressione ENTER para jogar novamente", True, imports.green)
        else:
            imports.dis.blit(imports.game_over_img, (imports.dis_width/2 - imports.game_over_img.get_width()/2, imports.dis_height/2 - imports.game_over_img.get_height()/2))
            text = imports.font_style.render("Pressione ENTER para jogar novamente", True, imports.green)
        
        # Eixo X: É calculado como dis_width/3, ou seja, um terço da largura total da tela. Isso posiciona o texto aproximadamente um terço do caminho a partir da margem esquerda da tela.
        # Eixo Y: É definido como dis_height - 100, que posiciona o texto 100 pixels acima do final da altura da tela.
        # Em resumo, esse cálculo posiciona o texto de forma que ele fique na parte inferior da tela, deslocado um terço da largura a partir da esquerda.
        imports.dis.blit(text, [imports.dis_width/3, imports.dis_height - 100])
        imports.pygame.display.update()
        
        # Aguarda o evento de pressionar ENTER ou fechar a janela
        for event in imports.pygame.event.get():
            # Se o evento for imports.pygame.QUIT, ou seja, se o jogador fechar a janela, a função retorna False para indicar que o jogo não deve ser reiniciado.
            if event.type == imports.pygame.QUIT:
                return False
            # Se o evento for imports.pygame.KEYDOWN, verifica se a tecla pressionada foi ENTER (imports.pygame.K_RETURN). Se sim, a função retorna True para indicar que o jogo deve ser reiniciado.
            if event.type == imports.pygame.KEYDOWN:
                if event.key == imports.pygame.K_RETURN:
                    return True
