# Comunicação entre processos

Frequentemente, processos precisam comunicar-se entre si. Esse resumo trata-se sobre os aspectos relatviso sobre IPC (InterProcess Comunnication).

# Race Conditions

Processos que estão trabalhando em conjunto geralmente utilizam uma memória comum como forma de comunicação, na qual cada processo pode ler ou escrever dados. 

Imaginando um exemplo de spool (simultaneous peripheral operation on-line) de impressão. Quando um processo quer imprimir um arquivo, é inserido o nome do arquivo em uma lista especial, chamada de diretório de spool. Outro processo, responsável pela impressão, verifica esse diretório periodicamente e se houver arquivos, eles são impressos e seus nomes são retirados do diretório.

Pensando em um diretório que tenha muitas entradas, numeradas como 0, 1, ..., cada uma armazenando o noem do arquivo. É possível existir 2 variáveis compartilhadas: iSaida, que aponta para o nome do próximo arquivo a ser impresso, e iEntrada, que aponta para a proxíma entrada livre do diretório. Em um determinado instante, as entradas 0, 1 e 2 estão vazias (arquivos já foram impressos) e as entradas 3 e 4 estão ocupadas (na fila para impressão). Supondo que, simultaneamente, os processos A e B decidem isnerir no diretório o nome de um arquivo para impressão:

O processo A lê a variável iEntrada e armazena o valor lido, em alguma de suas prórprias variáveis internas (por exemplo, iEntradaLivre). Depois dessa operação ser concluída, ocorre o chaveamento do processo A para o B. Nesse momento, o processo B, também lê a variável iEntrada e pega o mesmo valor 5, armazenando o nome do arquivo nessa entrada e atualiza o valor de iEntrada para 6. Depois, com o chaveamento retornando para o processo A, ao consultar sua variável interna "iEntradaLivre", na qual salvou o valor lido no início do processo, encontra o valor 5. Então, armazena o nome do arquivo que deseja imprimir por cima do arquivo anteriormente escrito pelo processo B e atualiza o valor da variável iEntrada para 6. Dessa forma, o processo B nunca vai ter seu arquivo impresso.

# Regiões Críticas

A questão central para evitar problemas em qualquer tipo de compartilhamento (posições de memória RAM, arquivos etc) é encontrar uma forma de proibir que mais de um processo acesse o dado compartilhado ao mesmo tempo. Dessa forma, é necessário implementar uma forma de impedir que processos distintos acessem dados que envolvem riscos.

É necessário identificar quais são essas regiões de riscos. É apenas durante a execução dessa região que as exclusões mútuas são aplicadas, bloqueando o acesso dessa área. Assim, a performance não é tão afetada, pois o acesso só é limitado pontualmente, não bloqueando o processo como um todo.

Definido as regiões de riscos, cuja execução pode levar à ocorrência de race conditions, podemos passar a chama-lás de regiões críticas (ou seções críticas).  Assim, se nunca for permitido que dois ou mais processos estejam executando suas respectivas regiões críticas simultaneamente, são evitáveis as ocorrências de race conditions.

Para permitir processos que trabalham em conjunto cooperarem de maneira correta e eficiente na utlização de recursos compartilhados, é necessário garantir que quatro condições sejam satisfeitas:

- Dois ou mais processos não podem estar simultaneamente dentro de suas respectivas regiões críticas.
- Nenhuma consideração pode ser feita sobre a velocidade relativa de execução dos processos ou sobre o número de processadores disponíveis no sistema.
- Nnehum processo que esteja em execução fora de sua região crítica pode bloquear a execução de outro processo.
- Nenhum processo pode esperar indefinidamente para entrar em sua região crítica.

# Exclusão mútua

## Inibição das interrupções

A solução mais simples para construção da exclusão mútua de execução é obtida por hardware. Ela consiste em fazer com que cada processo desabilite as interrupções logo apóis seu ingresso em uma região crítica, habilitando-as outra vez imediatamente antes de deixá-la. Com as interrupções desabilitadas, o processo não poderá ser interrompido, já que o processador é cahveado entre processos por meio de interrupções de tempo. Logo, não haverá chaveamento de processos.

Embora essa solução funcione, não é recomendada. Não é uma boa prática dar aos processos de usuário o poder de desabilitar interrupções. Caso um desses processos desabilite a interrupção e não a habilite novamente, o usuário terá a impressão de que o computador está travado, pois o processador não será capaz de identificar teclas pressionadas no teclado, cliques no mouse, e-mails recebidos, etc. nenhm evento de E/S enquanto a interrupção permanecer desabilitada.

## Variáveis de travamento

Uma segunda tentativa de construção de exclusão mútua de exceção é obtida por software. Considere a existência de uma única variável compartilhada (chamada variável de travamento), cujo valor seja inicialmente 0. Quando um processo desejar entrar em sua região crítica, ele deve primeiro testar o valor da variável. Se ela for 0, o processo muda seu valor para 1 e entra em sua região crítica. Se for 1, o processo deve esperar que ela volte para 0 antes de entrar em sua região crítica.

Essa solução pode apresentar a mesma falha do diretório de spool. Supondo que um processo leia a variável de travamento e verifique que seu valor é 0. Antes que ele possa atualiza-lá para 1, ocorre uma interrupção de tempo e outro processo passa a ser executado. Esse outro processo encontra a variável de travamento em 0, atualiza seu valor para 1 e entra em sua região crítica. Acontece que o processo interrompido guardou em seu contexto o valor 0 para a variável, de modo que, ao retornar sua execução, ele atualizará seu valor para 1 e entrará em sua região crítica. Então, dois processos poderão executar suas respectivas regiões críticas simultaneamente.

## Solução de Peterson

Em 1981, Gary L. Peterson propôs uma forma de obter a exclusão mútua. O "Algoritmo de Peterson", como é mostrado á seguir, implementa da seguinte forma:

Antes de executar sua respectiva região crítica, cada processo deve chamar a função EntrarNaRegiãoCritica(), com seu próprio número de identificação do processo (PID) como parâmetro. Essa chamada vai fazer com que o processo espere até que seja seguro entrar em sua região crítica. Quando o processo terminar a execução, ele deve chamar a função SairDaRegiaoCritica(), permitindo, assim, a entrada deoutro processo em sua respectiva região.

```python
# Constantes
FALSE = 0
TRUE = 1
NUMERO_DE_PROCESSOS = 2

# Variável compartilhada
iInteresse = [NUMERO_DE_PROCESSOS]

def EntrarNaRegiaoCritica(iProcesso):
    print(f"Processo {iProcesso} tentando entrar na região crítica...")

    # Obtém o outro processo
    iOutro = 1 - iProcesso

    iInteresse.insert(iProcesso, TRUE)
    print(f"Processo {iProcesso} sinalizou interesse.")

    iVez = iProcesso
    print(f"Flag de vez definida para {iVez}.")

    while iVez == iProcesso and iInteresse[iOutro] == TRUE:
        print(f"Processo {iProcesso} aguardando sua vez ou interesse do outro processo.")

    print(f"Processo {iProcesso} entrou na região crítica.")

def SairDaRegiaoCritica(iProcesso):
    print(f"Processo {iProcesso} saindo da região crítica.")

    iInteresse.insert(iProcesso, FALSE)
    print(f"Processo {iProcesso} sinalizou saída.")

# Simulação de acesso à região crítica
for iProcesso in range(NUMERO_DE_PROCESSOS):
    EntrarNaRegiaoCritica(iProcesso)
    print(f"Processo {iProcesso} executando código na região crítica.")
    SairDaRegiaoCritica(iProcesso)
```

O problema dessa solução, é que o processo fica em estado de aguarde, o que pensando em uma aplicação, significa que o usuário ficaria preso até o processo do usuário anterior ser liberado.

## Instrução TSL

Uma forma de construção de exclusão mútua de execução por hardware utiliza uma instrução denominada TEST AND SET LOCKED (TSL), que transfere o conteúdo de um endereço de memória para um registrador e depois armazena um valor diferente de zero nesse endereço de memória. As operação de transferência e armazenamento são indivisíveis, nenhum outro processo ou processador pode acessar o endereço de memória em questão antes que a execução da instrução TSL termine. O processador que estiver executando a instrução TSL bloqueia o barramento de memória até o término da execução da instrução.

Para a execução, é necessária a utilização de uma variável compartilhada. No código a seguir, são apresentadas duas sub-rotinas em Assembly, que utilizam uma variável compartilhada denominada flag.

Quando a flag for igual a 0, qualquer processo pode defini-la como 1, pela execução da instrução TSL e acessar a memória compartilhada. Ao terminar o acesso, o próprio processo em execução faz a variável flag igual a 0 utilizando a instrução mov.

Pode ser utilizada em máquinas com vários núcleos de processamento. Um processador pode impedir que os demais processadores tenham acesso à memória compartilhada enquanto não terminar seu acesso.

```assembly
enter_region:
tsl register,flag ;faz register = flag e flag = 1
cmp register,0 ;flag!=0?
;sim, prende o processo nesta sub-rotina
jnz enter_region
;retorna a quem chamou
;(ou seja, entra na região crítica)
ret
leave_region:
mov flag,0 ;faz flag=0
ret ;retorna a quem chamou
```