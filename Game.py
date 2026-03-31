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


def report_example(self):
        '''
        Relatório contendo:

        (ok)A informação de que o ladrão escapou ou se foi preso e em quantas etapas;

        Número de equipes de policiais necessários para prender o ladrão, em caso de sucesso;

        Sequência de vértices visitados pelo prisioneiro;

        Se ocorreu, o momento em que os policiais o alcançaram;

        Caminho percorrido pelos policiais durante a perseguição;

        '''
        print("-x-x-x-x--Relatorio--x-x-x-x-")
        if self.winner:
            print("->A fulga foi um sucesso !!!")
        elif self.loser:
            print("-> O ladrao foi pego...")
        else:
            print("Fim de Simulação")
        
        print("Caminho percorrido pelo bandido: ")
        print("-> ".join(self.thief_log ))

        #Gente aqui é durante e apenas durante a perseguição
        print("Caminho percorrido pelos policiais: ")
        for p, position, in enumerate(self.police_log):
            print(f"Etapa {p}: {position}")

        print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")