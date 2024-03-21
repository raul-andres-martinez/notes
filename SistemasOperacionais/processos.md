 # Conceituação de processo

 Inicialmente, um processo pode ser considerado como um programa em execução. Todo software que é executado por um computador, inclusive o próprio sistema operacional, é organizado como um ou mais processos.

 A maioria dos computadores novos são equipados com processadores, com vários núcleos de processamento, chamados processamentos multinúcleo (multicore), isto é, com chips contendo vários núcleos de processamento em seu interior. Os conceitos desta anotação consideram apenas computadores com um único processador.

 ## Multiprogramação

 ### Como um computador pode executar várias aplicações se há apenas um processador?

 O processador é chaveado entre vários programas em execução, ou seja, entre vários processos. Isto é chamado de multiprogramação.

 Nos sistemas com multiprogramação, o processador é chaveado entre diversos programas em execução, dando a cada programa dezenas de milésimos de segundos de processamento. Em todo
 sistema operacional, há um módulo de software chamado gerenciador de processos, cujo objetivo é fazer valer a multiprogramação no sistema computacional.

 Embora em um determinado instante apenas um programa esteja em execução, no decorrer de um segundo o processador pode ter trabalho para diversos programas, dando a ilusão aos usuários de paralelismo de execução (ou paralelismo aparente).

 Exemplo: Em uma operação de backup, são copiados vários arquivos para sua pasta Dropbox, mas ao mesmo tempo em que os arquivos estão sendo movimentados através do Windows Explorer, seu serviço Dropbox está sincronizando seus arquivos nos servidores. Isso só é possível porque o sistema operacional alterna a execução desses dois processos na CPU. Quando o Windows Explorer estiver em execução, o serviço Dropbox estará aguardando apra ser executado. Assim que o Windows Explorer deixa de ser executado, o serviço Dropbox entrará em execução.

 Porém o Windows Explorer não precisa ser executado até o fim para que o Dropbox seja selecionado para execução. O que ocorre é um fatiamento de cada processo. O Windows Explorer é selecionado, entra em execução, uma parte dele é processada durante uma dezena de milissegundos, depois ele é retirado da CPU para dar lugar ao Dropbox. Esse fica em execução durante um tempo similar e é retirado da CPU. Então, o Windows Explorer volta a ocupar a CPU, uma nova parte (subsequente à anterior) dele é executada durante um tempo. Após esse período, ele é retirado da CPU para, novamente, dar a vez ao serviço Dropbox. Esse processo se repete de forma alternada no uso da CPU, pedaço a pedaço, até terminar suas respectivas tarefas.

 Com o processador sendo chaveado entre diversos processos, verifica-se que a velocidade de execução de um determinado processo não é sempre similar e, dificlmente, em um mesmo computador, o mesmo processo é executado duas vezes, gastando, igualmente, o mesmo tempo de execução. Por esse motivo, a programação de processos não pode ter restrições de tempo. A execução total de um processo vai demorar o tempo que o sistema computacional, no cenário que se apresenta naquele instante de operação, tiver condições de executá-lo, alternando-o na CPU com os demais processos vigentes. A exceção fica por conta de processos que devem rodar em tempo real, que requer alguns cuidados especiais durante sua programação.
 
 ## Hierarquia de processos
 Um processo pode criar outros processos de maneira hierárquica. Quando um processo pai, cria outro processo, chamamos este de subprocesso ou processo filho. 

 Dependendo do sistema operacional, caso o processo pai termine, os subprocessos subordinados serão eliminados (Unix) ou não (Windows).

<img src="https://imgur.com/a/ZsAzo5Z" alt="Representacao de Subprocessos">

 Como exemplo, um browser. Normalmente um documento Web consiste em um arquivo HTML que contém
 texto comum acompanhado de imagens, ícones, aúdios, etc. Para buscar cada elemento, o browser tem de estabelecer uma conexão TCP/IP, ler os dados que chegam e passá-los ao componente de exibição. Assim, para melhorar o desempenho, o browser (processo pai) pode criar diversos processos filhos, de modo que, enquanto o processo pai exibe o texto, à medida que os dados vão chegando, os processos filhos continuam buscando outros arquivos da página.

 ## Estrutura de um processo

Um processo é constituído por três partes: contexto de hardware, contexto de software e espaço de endereçamento. Em conjunto, essas partes mantêm todas as informações necessárias à execução de um programa.

### Contexto de hardware

O contexto de hardware armazena o conteúdo dos registradores do processador. Quando um processo está em execução, o seu contexto de hardware está armazenado nos registradores do processador. No momento em que o processo perde a utilização do processador para outro processo, o sistema salva essas informações na memória principal. As alterações ocorrem nos registradores SP - Stack Pointer e IP - Instruction Pointer, à medida que o processo foi sendo executado.

Por exemplo, em um videogame, o seu usário cadastrado guarda todo o seu histórico de perfomance no jogo. Ao entrar em execução, é necessário que todas as informações atuais sobre pontuações, armas, quantidade de vida, etc, sejam carregadas fisicamente nos registradores da máquina. Assim, a CPU consegue trabalhar com essas informações por meio de operações de acesso aos registradores físicos.

No instante de tempo seguinte, no qual o sistema operacional retira o processo do videogame da CPU para alocar a ela outro processo, todas essas informações do seu usuário, manipuladas durante o processamento naquele instante de tempo anterior, são armazenadas na memória principal do comptuador para que, na próxima vez que esse processo entrar em execução, o jogo continue do ponto em que parou, com suas informações todas atualizadas. Enquanto estiverem armazenadas na memória principal, essas informações formam parte do contexto de hardware. Isso perdura e fica sendo atualizado durante toda a vigência do processo do jogo.

### Contexto de software

O contexto de software especifica características do processo e limites de recursos que podem ser alocados por esse processo, ele é composto por três grupos de informações: identificação, quotas e privilégios. Por exemplo, o processo do jogo, ao ser criado, recebe uma identificação, que é unica em todo o sistema computacional. Além disso, esse processo recebe quotas de utilização e quais são seus privilégios de acesso no sistema.

A identificação única é representada por um número **(PID - Process IDentification)**. Por meio do PID, o sistema operacional e outros processos podem referenciar qualquer processo existente. Alguns também conseguem identificar um processo por meio de um nome. Além disso, no momento de sua criação, atribui-se ao processo a identificação do usuário ou do processo que o está criando. Cada usuário possui uma identificação única no sistema **(UID - User IDentification)**. A UID permite construir um modelo de segurança, no qual apenas os objetos - processos, arquivos, áreas de memória, etc. - que possuam a mesma UID, podem ser acessados por um determinado usuário.

Quando você inicializa o videogame, um novo processo é criado sob a responsabilidade do seu usuário. Esse processo é o próprio programa do jogo que passa a ser gerenciado pelo sistema operacional. Então, esse processo recebe um PID e é vinculado a um UID. Também se associa a ele o PID do seu processo pai, que emitiu oficialmente a chamada de sistema que requisitou a abertura e execução do jogo.

As quotas representam os limites de cada recurso do sistema computacional que um processo pode alocar. Alguns exemplos são: número máximo de arquivos abertos simultaneamente, tamanho máximo de memória principal e secundária para as quais o processo pode solicitar alocação, número máxima de operações de E/S pendentes, tamanho máximo do buffer para operações de E/S e número máximo de subprocessos que podem ser criados. Ao rodar o jogo, o processo que o representa recebe essa quota, ou seja, a sua diretriz de uso do sistema. Assim, as quotas estabelecem todo o limite de utilização dos recursos computacionais, enquanto ele estiver ativo.

Os privilégios (ou direitos) definem as ações que um processo pode fazer em relação a si próprio, em relação aos demais processos e em relação ao sistema operacional. Privilégios que afetam o próprio processo permitem que suas características possam ser alteradas: prioridade de execução, tamanho máximo de memória principal e secundária para as quais o processo pode solicitar alocação etc. Privilégios que afetam o sistema operacional são os mais amplos e poderosos, uyma vez que eles estão relacionados à operação e à gerência do sistema: desativação do sistema computacional, alteração de regras de segurança, criação de outros processos privilegiados e alteração de parâmetros de configuração do sistema computacional.

A maioria dos sistemas operacionais possui uma conta de acesso com todos esses privilégios disponíveis. Como exemplos de contas com esse perfil existem a conta root no sistema operacional Unix e a conta administrador no sistema operacional Windows.

Na imagem a seguir, são mostradas algumas quotas do processo WINWORD.EXE, identificado pelo ID 7670. Possuí informações como seu nível de prioridade (Priority 8), o tamanho disponível em sua memória virtual (Virtual Size, 698.444 K) e seu espaço de endereçamento (Working Set, 106.960 K), entre outras informações. O espaço de endereçamento representa a área de memória pertencente ao processo em que as instruções e os dados do programa são armazenados para execução. Cada processo possui seu próprio espaço de endereçamento, que é protegido, pelo sistema operacional, do acesso pelos demais processos.

<img src="https://imgur.com/a/HXdNL1a" alt="Processo WINWORD">

 A troca de um processo para outro na CPU é gerenciada pelo sistema operacional e é denominada
 troca de contexto. Consiste, principalmente, em salvar o conteúdo dos registradores do processo que está deixando a CPU e carregar o conteúdo dos registradores do novo processo que será executado.

<img src="https://imgur.com/a/wKwOeW1" alt="Troca de Contextos">

 Pensando que você está executando um videogame, mas também escrevendo no Word um trabalho, teremos dois processos competindo pela utilização da CPU. Os dois processos vão sendo colocados em execução, de forma alternada. A cada troca de processo na CPU, ocorre a troca de contexto. Caso o Word seja retirado da CPU para que o jogo entre em execução, as informações referentes ao estado atual de utilização do Word precisam desocupar os registradores físicos para dar espaço ao jogo. Os dados que estão sendo retirados, para não serem perdidos, são salvos na memória principal do computador. E os dados que estão sendo carregados para processamento são lidos da memória principal e copiados nos registradores físicos da CPU.

 ## Bloco de controle de processo

 Cada processo é gerenciado por meio de uma estrutura de dados chamada bloco de controle de processo (PCB - Process Control Block), a partir da qual o sitema operacional mantém todas as informações sobre o contexto de hardware, software e o espaço de endereçamento do processo. Para cada PID há um PCB com todo o montante de informação sobre o processo.

 ## Escalonamento de processo

 Em um sistema com multiprogramação, um processo não permanece em execução no processador durante todo o tempo, ora o processo está em execução, ora está aguardando para retormar sua execução. Podemos dizer que, durante sua existência, um processo passa pelos seguintes estados:

 - Execução ou Rodando (Running): Quando o processo está usando o processador naquele instante.
 - Pronto (Ready): Quando o processo está em condições de ser executado, mas temporariamente parado, para dar vez a outro processo.

 Além desses dois estados, há um terceiro processo, em que o processo não pode ser executado, mesmo que o processador esteja disponível e não tenha nenhuma outra tarefa para executar:

- Espera ou Bloqueado (Wait): Quando o processo está impedido de ser executado até que ocorra um determinado evento externo ao processo.

Um processo está no estado Bloqueado quando ele está esperando pela realização de alguma operação imprescindível para continuidade de sua execução, normalmente, uma operação de E/S.

Por exemplo, um proceso A é executado pela CPU durante 100ms, após 20 ms de execução, ele solicita a leitura de um arquivo. Não há motivo para manter esse processo A na CPU, já que para sua continuidade, é necessário que o arquivo seja lido.

Dessa forma, existem quatro transições entre os três estados de um processo.

A transição 1 ocorre quando o processo não tem mais condições lógicas de prosseguir em seu processamento.

As transições 2 e 3 ocorrem ao mesmo tempo e são controladas por um múdulo do sistema operacional chamado escalonador de processos (ou scheduler).

A transição 2 ocorre quando o escalonador decide que o processo corrente já ocupou o processador por tempo suficiente, sendo, portanto, o momento de permitir que outro processo seja executado.

A transição 3 ocorre quando for o momento de executar o próximo processo que está aguardando pela CPU na fila de processos prontos.

Já a transição 4 ocorre quando acontece o evento externo pelo qual o processo estava aguardando, por exemplo, a conclusão de uma operação de E/S.

A transição 1 é provocada pelo próprio processo em execução, na maioria das vezes, quando o processo solicita ao SO, por meio de uma chamada de sistema (system call), a execução de uma operação de E/S. Para execução das transições 2 e 3, o escalonador de processos utiliza interrupção geradas pelo temporizador (timer) da CPU. A transição 4 ocorre quando a operação de E/S solicitada por um determinado processo é concluída, o que, normalmente, é sinalizado por uma interrupção.

Quando mais de um processo está pronto para ser executado, o sistema operacional deve decidir qual deles vai ser executado primeiro.

### Round Robin

O algoritmo utilizado na programação do escalonador é chamado de algoritmo de escalonamento. Esse algoritmo garante:

- Justiça: Garantir que todos os processos do sistema tenham oportunidade iguais de utilização do processador.
- Eficiência: Manter o processador ocupado a maior parte do tempo.

Um desses algoritmos mais antigos, simples e justo, é o algoritmo de escalonamento circular (round robin), no qual, pra cada processo atribui-se um intervalo de tempo chamado fatia de tempo (time-slice ou quantum (Q)), durante qual processo pode utilizar o processador. Assim que a fatia de tempo termina, o processo perde o processador, dando lugar a outro processo. Se o processo for bloqueado ou acabar antes do término de sua fatia de tempo, a comutação ocorrerá no exato momento do bloqueio ou do término do processamento.

É muito simples de ser implantado, tudo o que o escalonador precisa fazer é manter uma lista de processos prontos para serem executados.

O programa a seguir associa o escalonamento circular à situação de uma fila em um banco. O caixa é a CPU, e as pessoas na fila são os processos. Cada processo precisa pagar uma quantidade de faturas para terminar sua execução, ou seja, usar a CPU por um determinado tempo. Porém, o caixa só permite que cada pessoa pague certo número de faturas de cada vez. Essa quantidade é o quantum e representa a fatia de tempo. Se o processo terminar sua execução (todas as contas foram pagas), a pessoa sai da fila. Se não, volta ao final da fila e espera sua vez, novamente.

```python
def criarContas():
    contas = []
    for i in range(1, qtdPessoas + 1):
        print(f"Digite o número de contas a pagar da pessoa {i}: ")
        qtdContas = int(input())
        contas.append(qtdContas)
    return contas

def fila():
    contador = qtdPessoas
    posicao = 0
    while contador > 0:
        for i in range(0, qtdPessoas):
            if pessoas[i] > 0:
                print(f"A pessoa {i + 1} vai para o caixa com {pessoas[i]} contas.")
                print(f"Paga até {quantum} contas.")
                aux = pessoas[i] - quantum
                pessoas[i] = aux
                if aux <= 0:
                    print("E sai da fila.")
                    contador -= 1
                else:
                    print(f"E vai pro final da fila com {aux} contas.")
            posicao = (posicao + 1) % qtdPessoas

print("Digite o número máximo de contas a pagar no caixa (quantum): ")
quantum = int(input())
print("Digite o número de pessoas na fila: ")
qtdPessoas = int(input())
pessoas = criarContas()
fila()
print("Fim!")

```

A dificuldade de projeto reside na determinação do tamanho da fatia de tempo. Quando o processador é chaveado de um processo para outro, gasta-se algum tempo em tarefas necessárias à execução correta do sistema: salvar e restaurar registradores e mapas de memória, atualizar as várias tabelas e listas etc.

Pensando em um algoritmo com uma fatia de tempo de 20 ms e que a troca de contexto gaste 5ms. Dessa forma, após trabahar 20ms em uma tarefa útil, o processador vai gastar 5 ms na troca de contexto. 20% do tempo de processador serão gastos na administração do sistema (sobrecarga (S) (overhead)). Para melhorar a eficiência do processador, o algoritmo de escalonamento circular deveria ter uma fatia de tempo de 500ms, o que representaria uma sobrecarga menos que 1%. Contudo, se tivermos dez processos prontos para serem executados, o último processo vai esperar, aproximadamente, 5sd (10x500ms = 5000ms ou 5s) para ter a chance de utilizar o processador.

Geralmente, uma fatia de tempo da ordem de 100ms apresenta uma boa solução de compromisso.

A principal vantagem do algoritmo de escalonamento circular é não permitir que um processo monopolize o processador, sendo o tempo máximo alocado continuamente igual à fatia de tempo definida no sistema.

