from graph.Create_graphos import Dgraphs

class Game:
    def __init__(self):
        self.winner = False
        self.loser = False
        self.steps = 0 

    def game_simulation(self, graph: Dgraphs):
            '''
                inicializa historico de passos 
                Primeiro o ladrao se move
                Dps o policial se move(entra em perseguição ).
                atualiza historido de passos
                Dps verificamos se o ladrao foi pego ou se escapou.

                '''
            perseg = False

            graph.thief_log.append(graph.thief.position)
            graph.police_log.append(list(graph.police.positions))

            while True:
                self.steps += 1

                graph.police.move(graph.thief.position, perseg) 

                graph.police_log.append(list(graph.police.positions))
                
                if graph.police.positions in graph.thief.position:
                        graph.winner = True
                        print("O ladrão foi pego! A polícia venceu!")
                        break

                clear_path = graph.thief.move()

                if clear_path:
                    graph.thief_log.append(graph.thief.position)
                    perseg = True
                    
                    if graph.thief.position in graph.ports.ports:
                        graph.loser = True
                        print("O ladrão escapou pelos portos! O ladrão venceu!")
                        break
            

    
    def criar_relatorio(self,relatorio, arquivo):
        print(relatorio)
        arquivo.write(relatorio + "\n")   


    def report_example(self, graph: Dgraphs):
            with open("Relatorio.txt", "w", encoding="utf-8") as f:

                '''
                Relatório contendo:

                (ok)A informação de que o ladrão escapou ou se foi preso e em quantas etapas;

                (ok) Número de equipes de policiais necessários para prender o ladrão, em caso de sucesso;

                (ok) Sequência de vértices visitados pelo ladrão;

                (ok) Se ocorreu, o momento em que os policiais o alcançaram;

                (ok) Caminho percorrido pelos policiais durante a perseguição;

                '''

                self.criar_relatorio("-x-x-x-x--Relatorio--x-x-x-x-",f)
                #relatorio ladão
                if self.winner:
                    self.criar_relatorio("->A fulga foi um sucesso !!!", f)
                    self.criar_relatorio(f"->O ladrão escapou em {self.steps} etapas.", f)
                elif self.loser:
                    self.criar_relatorio("-> O ladrao foi pego...", f)
                    self.criar_relatorio(f"->O ladrão foi pego em {self.steps} etapas.", f)
                else:
                    self.criar_relatorio("Fim de Simulação", f)


                self.criar_relatorio("Caminho percorrido pelo bandido: ", f)
                self.criar_relatorio("-> ".join(graph.thief_log ), f)


                #relatorio policia
                if graph.police.police_team:
                    self.criar_relatorio(f"-> Número de equipes policiais: {graph.police.police_team}", f)

                #Gente aqui é durante e apenas durante a perseguição
                self.criar_relatorio("Caminho percorrido pelos policiais: ", f)
                for p, position, in enumerate(graph.police_log):
                    self.criar_relatorio(f"Etapa {p}: {position}", f)

                #relatorio da captura
                if self.loser:
                    for p, positions in enumerate(graph.police_log):
                        if graph.thief_log[p] in positions:
                            self.criar_relatorio(f"\n-> Captura ocorreu na etapa {p} no nó {graph.thief_log[p]}", f)
                            break

                self.criar_relatorio("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-", f)
