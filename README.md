# Trabalho de Algoritmos em Grafos 
## Requisitos do Projeto
Deve-se implementar, em linguagem de programação de sua escolha (Python, C++, Java, etc.), um sistema que:
1. Representação da ilha
* A ilha deve ser representada como um grafo ponderado G = (V,E).
* A entrada do programa será um arquivo de texto descrevendo:
  - Número de vértices |V| = n;
  - Número de arestas |E| = m;
  - Lista de arestas no formato: u v w(u,v) (significa aresta entre vértices u e v com peso w(u,v));
  - Vértice que representa o local do roubo;– Vértices de saída da ilha, diferentes do local do roubo;
  - Quantidade e posições iniciais das equipes de polícia;– Considere que a quantidade de equipes policiais é sempre menor que a soma dos graus de entrada de
    cada vértice representando uma saída da ilha, de modo que sempre há uma rota de fuga para o ladrão.

2. Objetivo: Executar as dinâmicas de movimentações do fugitivo e dos policiais. Caso o ladrão não tenha como
escapar para um vértice vizinho qualquer sem se deparar com a polícia, então o mesmo será capturado.

## Movimentação
* Ladrão:
  *  Move-se um vértice por vez;
  *  Se encontrar alguma saída em qualquer momento, o programa deve indicar que o ladrão conseguiu escapar
    e tentar prendê-lo utilizando outra estratégia ou mais policiais.
* Policiais:
  * Move-se normalmente um vértice por vez ao longo da ilha, em patrulhas sem ocorrências de roubo;
  * Durante a perseguição, move-se dois vértices por rodada pelo caminho mínimo atual em direção ao ladrão;
  * Se alcançar o mesmo vértice do ladrão antes deste encontrar a saída, o mesmo é preso.

## Saída
* Relatório contendo:
  *  Ainformação de que o ladrão escapou ou se foi preso e em quantas etapas;
  * Número de equipes de policiais necessários para prender o ladrão, em caso de sucesso;
  * Sequência de vértices visitados pelo prisioneiro;
  * Se ocorreu, o momento em que os policiais o alcançaram;
  * Caminho percorrido pelos policiais durante a perseguição;

