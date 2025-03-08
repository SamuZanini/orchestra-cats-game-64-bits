from src.settings.imports.imports import imports
from src.settings.display.menu import show_menu, show_end_screen

def our_cats(cat_size, cat_list, cat_types, current_conductor, current_musicians):
    if not cat_list:
        return
    
    for i, pos in enumerate(cat_list):
        if i == len(cat_list) - 1:  # Último elemento: cabeça
            imports.dis.blit(current_conductor, (pos[0], pos[1]))
        elif i < len(cat_types):  # Elementos do corpo
            imports.dis.blit(current_musicians[i % len(current_musicians)], (pos[0], pos[1]))

# Define quanto os gatos crescem a cada refeição
incremento_gatos = 1

def gameLoop():
    while True:
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
        
        game_over = False
        won = False
        
        x1 = imports.dis_width / 2
        y1 = imports.dis_height / 2

        x1_change = imports.cat_size  
        y1_change = 0
        
        cat_list = [[x1, y1]]
        cat_types = []
        length_of_cats = 1
        current_speed = imports.base_speed
        boost_end_time = 0
        
        foodx = round(imports.random.randrange(0, imports.dis_width - imports.cat_size) / imports.cat_size) * imports.cat_size
        foody = round(imports.random.randrange(0, imports.dis_height - imports.cat_size) / imports.cat_size) * imports.cat_size

        is_red_yarn = imports.random.random() < 0.2

        while not game_over:
            for event in imports.pygame.event.get():
                if event.type == imports.pygame.QUIT:
                    game_over = True
                elif event.type == imports.pygame.KEYDOWN:
                    if event.key == imports.pygame.K_LEFT:
                        x1_change = -imports.cat_size
                        y1_change = 0
                    elif event.key == imports.pygame.K_RIGHT:
                        x1_change = imports.cat_size
                        y1_change = 0
                    elif event.key == imports.pygame.K_UP:
                        y1_change = -imports.cat_size
                        x1_change = 0
                    elif event.key == imports.pygame.K_DOWN:
                        y1_change = imports.cat_size
                        x1_change = 0

            x1 += x1_change
            y1 += y1_change

            if x1 >= imports.dis_width or x1 < 0 or y1 >= imports.dis_height or y1 < 0:
                game_over = True
                won = False
                imports.pygame.mixer.music.stop()
                break
            
            # Usa o background apropriado para o gênero atual
            imports.dis.blit(current_bg, (0, 0))
            
            if is_red_yarn:
                imports.dis.blit(imports.yarn_red, (foodx, foody))
            else:
                imports.dis.blit(imports.yarn_gray, (foodx, foody))

            cat_head = [x1, y1]
            
            if cat_head in cat_list[:-1]:
                game_over = True
                won = False
                imports.pygame.mixer.music.stop()
                break
            
            cat_list.append(cat_head)
            
            if len(cat_list) > length_of_cats:
                del cat_list[0]
                if cat_types and len(cat_types) > length_of_cats - 1:
                    del cat_types[0]
            
            # Passa os sprites atuais para a função our_cats
            our_cats(imports.cat_size, cat_list, cat_types, current_conductor, current_musicians)
            
            imports.dis.blit(imports.yarn_gray_counter, (10, 10))
            score = imports.score_font.render(str(length_of_cats), True, imports.white)
            imports.dis.blit(score, (10 + imports.yarn_gray_counter.get_width() + 5, 10))
            
            imports.pygame.display.update()
            
            head_rect = imports.pygame.Rect(x1, y1, imports.cat_size, imports.cat_size)
            food_rect = imports.pygame.Rect(foodx, foody, imports.cat_size, imports.cat_size)
            if head_rect.colliderect(food_rect):
                foodx = round(imports.random.randrange(0, imports.dis_width - imports.cat_size) / imports.cat_size) * imports.cat_size
                foody = round(imports.random.randrange(0, imports.dis_height - imports.cat_size) / imports.cat_size) * imports.cat_size
                
                length_of_cats += incremento_gatos
                # Usa os músicos apropriados para o gênero atual
                cat_types.append(1)  # Apenas para manter o controle do comprimento
                
                if is_red_yarn:
                    current_speed = imports.base_speed + 2
                    boost_end_time = imports.time.time() + 3
                    is_red_yarn = False
                else:
                    is_red_yarn = imports.random.random() < 0.2

            if boost_end_time and imports.time.time() > boost_end_time:
                current_speed = imports.base_speed
                boost_end_time = 0

            imports.clock.tick(current_speed)
            
            if not imports.pygame.mixer.music.get_busy():
                game_over = True
                won = True
                break
        
        if not show_end_screen(won):
            break

    imports.pygame.quit()
    quit()

# Inicia o jogo chamando o loop principal
gameLoop()
