'''

    Nessa simulação, a policia e o ladão se movem em um grafo, onde os vértices representam locais e as arestas representam caminhos entre esses locais. 
    O jogo se inicia com os policiais fazendo as patrulhas tradicionais(andando de 1 em 1 vertice), apois o a primeira patrulha dos policiais, o ladrão faz seu primeiro movimento entrando no local do roubo.A partir disso, a persiguiçao começa, onde a policia entre em modo perseguiçao(andando de 2 em 2 vertices), a policia possui a posiçao do ladão e assim procurnado o menor caminho ate ele.
    O ladrão tenta escapar para um dos vértices de saída, enquanto a polícia tenta interceptá-lo. 
    A cada etapa, o ladrão pode escolher um caminho para se mover, vendo os melhores caminhos ate os portos.
    O jogo continua até que o ladrão seja capturado ou consiga escapar. 
    Durante a simulação, resgistrado o histórico de movimentos do ladrão e da polícia, bem como o número de etapas necessárias para alcançar ou a vitória ou derrota. 
    O relatório final inclui informações sobre o resultado do jogo, o número de equipes policiais envolvidas, a sequência de vértices visitados pelo ladrão, o momento da captura (se ocorrer) e o caminho percorrido pelos policiais durante a perseguição.
    
'''
from graph.Create_graphos import Dgraphs

class Game:
    def __init__(self):
        self.winner = False
        self.loser = False
        self.steps = 0 
        self.capture_step = None

    def game_simulation(self, graph: Dgraphs):
            '''
                inicializa historico de passos 
                Primeiro a policia se move
                Dps o ladão se move(entra em perseguição ).
                atualiza historido de passos
                Dps verificamos se o ladrao foi pego ou se escapou.

                '''
            print("-x-x-xINICIANDO SIMULAÇÃO-x-x-x-\n\n")

            perseg = False

            # graph.thief_log.append(graph.thief.position)
            # graph.police_log.append(list(graph.police.positions))

            while True:
                self.steps += 1
                print(f"\n[ETAPA {self.steps:02d}]")

                graph.police.move(graph.thief.position, perseg) 
                graph.police_log.append(list(graph.police.positions))
                print(f"POLICIA: moveu-se para {graph.police.positions}")

                if perseg:
                    if graph.thief.position in graph.police.positions:
                            self.winner = True
                            print(f"->O ladrão foi pego no nó {graph.thief.position}.")
                            print("RESULTADO: A polícia venceu!")
                            self.capture_step = self.steps
                            break
                #
                neigh_free = graph.thief.blockade()
                if not neigh_free:
                    self.winner = True
                    print(f"-> O ladrão NÃO tem rotas de fuga disponíveis.")
                    print(" RESULTADO: A polícia venceu por cerco!")
                    self.capture_step = self.steps
                    break
                #

                clear_path = graph.thief.move()

                if not clear_path:
                    self.winner = True
                    print("-> Ladrão sem movimentos possíveis.")
                    print(" RESULTADO: O ladrão se rendeu!")
                    self.capture_step = self.steps
                    # deu problema ele fica impossibilitado de se mover e nem como a policia chegar nele
                    print("Ladrão sem movimentos possíveis.")
                    break

                if clear_path:
                    graph.thief_log.append(graph.thief.position)
                    perseg = True
                    print(f"-> LADRÃO: Moveu-se para o nó {graph.thief.position}")

                    if graph.thief.position in graph.ports.ports:
                        self.loser = True
                        print(f" -> O ladrão alcançou o porto {graph.thief.position}.")
                        print(" RESULTADO: O ladrão escapou com sucesso!")
                        break
            print("\n")
            print("-x-x-x-SIMULAÇÃO FINALIZADA-x-x-x\n")
            self.report_example(graph)
                
            

    
    def criar_relatorio(self,relatorio, arquivo):
        print(relatorio)
        arquivo.write(relatorio + "")   


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
                print("")   
                self.criar_relatorio(f"{'[-x-x-x-x-x-x-x--RELATÓRIO--x-x-x-x-x-x-x-]':^50}",f)

                #relatorio ladrão
                if self.loser:
                    self.criar_relatorio("STATUS: A fulga foi um sucesso !!!", f)
                    self.criar_relatorio(f"-> O ladrão escapou em {self.steps} etapas.\n", f)
                elif self.winner:
                    self.criar_relatorio("STATUS: -> O ladrao foi pego...", f)
                    self.criar_relatorio(f"-> Captura realizada em {self.steps} etapas.\n", f)
                else:
                    self.criar_relatorio(" ->Empate...", f)

                #relatorio policia
                if hasattr(graph.police, 'police_team') and graph.police.police_team:
                    self.criar_relatorio(f"\n-> Número de equipes policiais: {graph.police.police_team}", f)

                self.criar_relatorio("CAMINHO: percorrido pelo bandido: ", f)
                self.criar_relatorio("-> ".join(graph.thief_log ), f)
        
                for p, thief_pos in enumerate(graph.thief_log):
                    police_positions = graph.police_log[p]
                    
                    # Formatação da lista de policiais
                    if isinstance(police_positions, list):
                        pos_str = ", ".join(map(str, police_positions))
                    else:
                        pos_str = str(police_positions)
                        
                    # Mostra o que cada um fez na etapa P
                    log_linha = f"Etapa {p:02d} | Ladrão: {thief_pos} | Policiais: [{pos_str}]"
                    self.criar_relatorio(log_linha, f)

                    # Se houve vitória e estamos no passo da captura, destaca no log
                    if self.winner and p == getattr(self, 'capture_step', -1):
                        self.criar_relatorio(f"O LADRÃO FOI CAPTURADO NO NÓ {thief_pos}!", f)
                
                    self.criar_relatorio(f"{'[-x-x-x-x-x-x-x--FIM DO RELATÓRIO--x-x-x-x-x-x-x-]':^50}", f)
                    pos_str = str(position)
                    self.criar_relatorio(f"Etapa {p}: [{pos_str}]", f)
                
                self.criar_relatorio("Caminho percorrido pelos policiais: ", f)

                num_police = max(len(etapa) for etapa in graph.police_log)

                for i in range(num_police):
                    caminho = []

                    for etapa in graph.police_log:
                        if i < len(etapa):
                            caminho.append(str(etapa[i]))
                    self.criar_relatorio(f"Policial {i+1}: " + " -> ".join(caminho), f)

                #relatorio da captura
                if self.winner:
                    for p, positions in enumerate(graph.police_log):
                        if graph.thief_log[p] in positions:
                            self.criar_relatorio(f"\n-> Captura ocorreu na etapa {self.capture_step} no nó {graph.thief_log[p]}\n", f)
                            break
                self.criar_relatorio("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-", f)
