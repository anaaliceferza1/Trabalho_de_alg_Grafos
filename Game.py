from graph.Create_graphos import Dgraphs

def game_simulation(graph: Dgraphs):
        '''
            inicializa historico de passos 
            Primeiro o ladrao se move
            Dps o policial se move(entra em perseguição ).
            atualiza historido de passos
            Dps verificamos se o ladrao foi pego ou se escapou.

            '''
        step = 0
        perseg = False

        graph.thief_log.append(graph.thief.position)
        graph.police_log.append(list(graph.police.positions))

        while True:
            step += 1
            #graph.steps = step

            #thief_move = graph.thief.move()

            graph.police.move(graph.thief.position, perseg) 
            
            if graph.police.positions in graph.thief.position:
                    graph.loser = True
                    print("O ladrão foi pego! A polícia venceu!")
                    break

            clear_path = graph.thief.move()
            
            perseg = True

            graph.thief_log.append(graph.thief.position)
            graph.police_log.append(list(graph.police.positions))

            if clear_path:
                if graph.thief.position in graph.ports.ports:
                    graph.winner = True
                    print("O ladrão escapou pelos portos! O ladrão venceu!")
                    break
