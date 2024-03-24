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