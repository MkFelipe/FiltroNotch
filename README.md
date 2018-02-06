Implementação e estudo de caso: Filtro Notch utilizando Python/Numpy

Renzo Magno Nogueira e Felipe Miertschink
Professor: Thiago Paixão
Processamento Digital de Imagens - 2013/2
 
Justificativas:
Pode-se entender filtragem de uma imagem, como sendo técnicas de transformações 
aplicadas a cada SL[HO da imagem, levando em conta os níveis de cinza de uma região vizinha 
de cada pixel desta imagem. 
As técnicas de filtragem podem ser divididas em dois tipos: filtragem no domínio 
espacial e filtragem no domínio da frequência. 
Neste artigo será implementado o filtro de frequência Notch. Antes disso, é válido discutir certos aspectos
do processamento de iamgens no domínio da frequência. Este processo pode ser basicamente dividido em 3 etapas:
 
1- a imagem é transformada do domínio espacial para o domínio da frequência, usando a 
transformada de Fourier; 
2- operações são realizadas nessa imagem; 
3- e para que a imagem possa ser exibida e vista por olhos humanas, ocorre o 
processo inverso, onde a imagem no domínio da freqüência é transformada para o domínio espacial. Sendo este último
passo feito pela transformada inversa de Fourier.
 
Notch: São filtros capazes de rejeitar uma faixa bastante estreita de frequências, atuando quase que exclusivamente na frequência selecionada e bem pouco nas outras ao redor. Sua utilização é recomendada quando o sinal a ser atenuado é bem definido. Pelo fato de atuar em faixas reduzidas de frequências, filtros notch interferem pouco na qualidade do sinal.
 
Os filtros notch são muito importantes para uma ampla variedade de aplicações de instrumentação, desde as telecomunicações ao processamento de sinais biomédicos, onde comumente é necessário remover uma banda estreita ou uma única frequência do sinal medido. A implementação analógica destes filtros sofre com a deriva dos componentes e consequente instabilidade do filtro, pelo que a implementação digital é preferível, até pela facilidade de projeto de filtros de ordem e fator de qualidade elevados. 

Conclusão:
 
Todavia, a implementação digital de filtros tem limitações na exatidão causadas em sua maioria pela precisão finita da aritmética. Devido à facilidade com que se projetam filtros IIR digitais de elevado desempenho, a resposta do filtro é tida como assegurada, mas, particularmente quando se lida com plataformas com aritmética de ponto fixo (microcontroladores, DSP e FPGA), ou com especificações de desempenho muito exigentes, a importância da exatidão dos coeficientes do filtro multiplica-se, podendo-se falhar completamente as especificações e distorcer o sinal. O filtro a seguir foi implementado com intuito de aprendizado. Utilizando-se de funções da biblioteca Numpy como a fft2 e ffshift o desenvolvimento acaba sendo um pouco facilitado, mas ainda sim com bom desempenho. É possível otimiza-lo, principalmente quando levado em consideração, um estudo de uma melhor janela de corte, e quais os melhores pontos candidatos a receber o filtro.


