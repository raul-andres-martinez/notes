
Máquina virtual: é uma visão de cima para baixo, na qual o sistema operacional é visto como uma extensão do hardware que fornece uma interface para as aplicações.

Gerente de recursos: é uma visão de baixo para cima, na qual o sistema operacional é visto como um controlador dos recursos do sistema.

Computadores operam de dois modos: o SO é executado no modo núcleo (kernel), com o objetivo de proteger o hardware da ação direta do usuário, já as aplicações são executadas no modo usuário.

Algumas instruções não podem ser colocadas diretamente à disposição das aplicações, visto que sua utilização indevida provocaria sérios problemas à integridade do computador. Por exemplo, uma aplicação que atualiza um arquivo no disco. Como o disco é um recurso compartilhado, sua utilização deve ser gerenciada exclusivamente pelo sistema operacional.

Assim, existem instruções que só podem ser executadas pelo sistema operacional (ou serem executadas sob supervisão). Essas instruções são conhecidas como instruções privilegiadas. Já as que não oferecem risco, são conhecidas como Instruções não privilegiadas.

Modos de acesso fazem sentido nesse contexto. Eles formam um mecanismo de proteção para controlar a execução das instruções privilegiadas. Quando o processador está no modo usuário, apenas instruções não privilegiadas podem ser executadas, enquanto no modo núcleo, todas as instruções do processador podem ser executadas.

A melhor forma de proteger o sistema é permitir que apenas o SO tenha acesso às instruções privilegiadas. Assim, quando um programa necessitar executar uma instrução privilegiada, essa solicitação será realizada por meio de uma chamada de sistema. Ao iniciar sua execução, a chamada de sistema altera o modo do processador de usuário para núcleo. Ao término de sua execução, a chamada de sistema retorna o modo de acesso para modo usuário.

Caso um programa tente executar uma instrução privilegiada diretamente no modo usuário, o processador sinalizará uma exceção.

Esse controle é feito com suporte do hardware. Um bit, chamado bit de modalidade, é adicionado ao hardware do processador para indicar o modo corrente: modo núcleo (bit de modalidade = 0) ou modo usuário (bit de modalidade = 1). É por meio deste bit que é possível distinguir se uma determinada instrução está sendo executada sob o controle do sistema operacional ou sob o controle de uma aplicação.

Durante a iniciação do sistema, o hardware começa a operar em modo núcleo. Quando é carregado e dá início aos processos do usuário, em modo usuário. Sempre que uma interrupção ou exceção ocorre, o hardware comuta do modo usuário para o modo núcleo, isto é, altera o valor do bit de modalidade de 1 para 0.

Comandos e chamadas de sistemas

O interpretador de comandos (shell) funciona como interface entre o usuário de um computador e o sistema operacional. Pode ser GUI ou CLI. Dependendo da versão do sistema operacional, o próprio interpretador de comandos é executado no modo usuário. Essa é a configuração que encontramos no Windows e no Unix, por exemplo.

As chamadas de sistema podem ser entendidas como uma porta de entrada para o acesso ao sistema operacional (núcleo do sistema operacional) e aos seus serviços. Sempre que uma aplicação necessita de algum serviço do sistema operacional, é feita uma chamada de sistema e, por meio dela, uma das rotinas de trabalho do sistema operacional é executada.

A denominação system calls é utilizada em sistemas UNIX. Em outros sistemas, o mesmo conceito é apresentado com diferentes nomes: system services, no OpenVMS e API no Windows.

Cada serviço disponível possui uma chamada associada, e cada sistema operacional tem seu próprio conjunto de chamadas de sistema, com nomes, parâmetros e modos de ativação específicos. Por isso, uma aplicação desenvolvida utilizando as chamadas de sistema de um determinado sistema operacional não pode ser portada diretamente para outro sistema operacional.

Proposta pela ISO e IEE, o padrão POSIX (Portable Operating System Interface for UNIX) foi criado para especificar conjuntos de chamadas de sistema padronizadas para serem executadas em qualquer sistema operacional que suporte o padrão POSIX. Inicialmente foi criado para a unificação das diversas versões do UNIX, posteriormente, foi incorporado pela maioria dos sistemas operacionais modernos.

Pelo fato do IEE cobrar pela documentação padrão do POSIX e não permitir sua publicação online, há uma nova tendência da especificação SUS (Single UNIX Specification), que é aberta.

As chamadas podem ser divididas em 5 categorias principais: controle de processos, gerenciamento de arquivos, gerenciamento de dispositivos, manutenção de informações e comunicações.

Então, pode-se dizer que o sistema operacional é formado por um conjunto de rotinas que oferece serviços aos usuários, às aplicações e ao próprio sistema computacional. Esse conjunto de rotinas é denominado núcleo do sistema operacional (kernel).

Vale ressaltar que é importante não confundir o núcleo do sistema operacional com as aplicações ou com o interpretador de comandos que acompanha o sistema operacional. As aplicações resolvem os problemas dos usuários e o interpretador de comandos permite aos usuários uma interação amigável com o sistema.

Os sistemas operacionais não possuem uma estrutura tipicamente sequencial, com início, meio e fim. Os procedimentos do sistema são executados concorrentemente e sem uma ordem predefinida, com base em eventos desassociados do tempo (eventos assíncronos). Muitos desses eventos estão relacionados ao hardware e às tarefas internas do próprio sistema operacional.

As principais funções do núcleo do sistema operacional são:

Tratamento de interrupções e exceções.
Gerência de aplicações em execução (processos).
Gerência de memória.
Gerência do sistema de arquivos.
Gerência de dispositivos de entrada e saída (E/S).
Suporte a redes locais e distribuídas.
Controle da utilização dos recursos do sistema computacional.
Funções de auditoria e segurança do sistema computacional.
A estrutura do sistema operacional, ou seja, como o código do sistema está organizado e o inter-relacionamento entre seus diversos componentes, pode variar conforme a concepção do projeto do sistema operacional.

Classificação dos sistemas operacionais

A evolução dos sistemas operacionais para computadores pessoais popularizou diversos conceitos e técnicas que eram antes conhecidas apenas em ambientes de grande porte, que foram adaptados para uma nova realidade.

Os primeiros sistemas foram projetados para a execução de um único programa. Dessa forma, para que outro programa pudesse ser executado, era necessário aguardar o término do programa corrente. Os sistemas monoprogramáveis ou sistemas monotarefa caracterizavam-se por permitir que o processador, a memória e os periféricos permanecessem exclusivamente à execução de um único programa.

Tipos de sistemas operacionais: Sistemas Monoprogramáveis ou Sistemas Monotarefa; Sistemas Multiprogramáveis ou Sistemas Multitarefa; Sistemas com Múltiplos Processadores. Sistemas Multiprogramáveis ou Multitarefa: Sistemas Batch; Sistemas de Tempo Compartilhado; Sistemas de Tempo Real.

Nos sistemas multiprogramáveis, os recursos computacionais são compartilhados por vários usuários e aplicações. Enquanto um programa espera por uma operação de entrada e saída (E/S), outro programa pode estar sendo processado ao mesmo tempo.

O sistema operacional é projetado para gerenciar, de forma ordenada e protegida, o acesso concorrente aos diversos recursos sob seu controle, ou seja, processador, memória e periféricos.

Os sistemas batch foram os primeiros tipos de sistema operacional multiprogramáveis. Os programas, que na época eram chamados de jobs, eram submetidos para execução por meio de cartões perfurados e armazenados em disco ou fita, aguardando para serem processados. Posteriormente, em função da disponibilidade de espaço na memória principal, os programas eram executados, produzindo uma saída em disco ou fita.

Para aumentar a velocidade de processamento, os operadores reuniam os jobs em lotes (batch) com requisitos semelhantes e os operavam no computador com um grupo.

O processamento batch caracteriza-se por não exigir a interação do usuário com a aplicação, isto é, todas as entradas e saídas de dados da aplicação são realizadas por algum tipo de memória secundária (disco ou fita).

Os sistemas de tempo compartilhado (timesharing) permitem que diversos programas sejam executados a partir da divisão do tempo do processador em pequenos intervalos de tempo denominados fatias de tempo (timeslices).

Nesses sistemas, cada programa tem direito de ser executado por uma fatia de tempo. Caso a fatia de tempo não seja suficiente para a conclusão do programa em execução, esse tempo é interrompido pelo sistema operacional, substituído por outro programa e permanece no aguardo de uma nova fatia de tempo para retomar sua execução. O sistema operacional cria um ambiente de execução próprio para cada programa, dando a impressão de que todo o sistema está dedicado exclusivamente àquele programa. Atualmente, a maioria dos sistemas operacionais comerciais se classifica como sistemas de tempo compartilhado.

Os sistemas de tempo real (real-time systems) são desenvolvidos de forma semelhante à dos sistemas de tempo compartilhado. A grande diferença é que os sistemas de tempo real são altamente acoplados ao mundo externo, isto é, devem responder no domínio do mundo físico, em uma escala ditada por esse e sob rigorosas restrições de desempenho. Por exemplo, os robôs da NASA em Marte utilizam esse tipo de sistema.

Dessa forma, nos sistemas de tempo real não existe a ideia de fatia de tempo, isto é, um programa utiliza o processador pelo tempo que for preciso ou até que apareça outro programa de maior prioridade. Além disso, a maioria das características avançadas de um sistema operacional está ausente nos sistemas de tempo real, já que tendem a separar o usuário do hardware, e tal separação resulta em incertezas quanto à quantidade de tempo que uma operação consumirá. Assim, nesses sistemas, são utilizados sistemas de tempo real (RTOS).

Os sistemas com múltiplos processadores caracterizam-se por possuir dois ou mais processadores trabalhando em conjunto. A vantagem desse tipo de sistema reside no fato de permitir que várias aplicações sejam executadas ao mesmo tempo ou que uma única aplicação seja subdividida em várias partes, para serem executadas simultaneamente em mais de um processador.

Desenvolveram-se, em grande parte, devido ao elevado custo de desenvolvimento de processadores de alto desempenho, sendo que as principais aplicações desses sistemas são encontradas, por exemplo, em áreas como o desenvolvimento aeroespacial e o processamento de imagens.