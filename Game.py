def game_simulation(self):
        '''
            inicializa historico de passos 
            Primeiro o ladrao se move
            Dps o policial se move(entra em perseguição ).
            atualiza historido de passos
            Dps verificamos se o ladrao foi pego ou se escapou.

            '''
        step = 0

        self.thief_log.append(self.thief.position)
        self.police_log.append(list(self.police.positions))

        while True:
            step += 1
            self.steps = step

            # thief_move = self.thief.move()

            self.thief.move()
            
            perseg = True

            self.police.move(self.thief.position, perseg)

            self.thief_log.append(self.thief.position)
            self.police_log.append(list(self.police.positions))
            
            if self.thief.position in self.police.positions:
                self.loser = True
                print("O ladrão foi pego! A polícia venceu!")
                break
            if self.thief.position in self.ports.ports:
                self.winner = True
                print("O ladrão escapou pelos portos! O ladrão venceu!")
                break
