''' Felipinho está empolgado com seu novo jogo de RPG sobre guerras entre clãs de vampiros. Nesse jogo ele representa um personagem de um vampiro e constantemente entra em conflito contra vampiros de outros clãs. Tais batalhas são realizadas com base nas características de cada personagem envolvido e com a ajuda de um dado comum de seis faces. Por simplicidade, vamos considerar apenas as lutas entre dois vampiros, vampiro 1 e vampiro 2. Cada um possui uma energia vital (chamaremos de EV1 e EV2 respectivamente) e, além disso, são determinadas uma força de ataque AT e uma capacidade de dano D.

O combate é realizado em turnos da maneira descrita a seguir. A cada turno um dado é rolado, se o valor obtido for menor do que ou igual a AT, o vampiro 1 venceu o turno, caso contrário o vampiro 2 é quem venceu. O vencedor suga energia vital do adversário igual ao valor D, ou seja, D pontos de EV são diminuídos do perdedor e acrescentados ao vencedor. O combate segue até que um dos vampiros fique com EV igual a ou menor do que zero.

Por exemplo, suponhamos que EV1=7, EV2=5, AT=2 and D=4. Rola-se o dado e o valor obtido foi 3. Nesse caso, o vampiro 2 venceu o turno e, portanto, 4 pontos de EV são diminuídos do vampiro 1 (EV1) e acrescentados ao vampiro 2 (EV2) Sendo assim, os novos valores seriam EV1=3 e EV2=9. Observe que se no próximo turno o vampiro 2 ganhar novamente, o combate irá terminar. Os valores de AT e D são constantes durante todo o combate, apenas EV1 e EV2 variam.

Apesar de gostar muito do jogo, Felipinho acha que os combates estão muito demorados e gostaria de conhecer de antemão a probabilidade de vencer, para saber se vale a pen a lutar. Assim, ele pediu que você escrevesse um programa que, dados os valores iniciais de EV1, EV2, além de AT e D, calculasse a probabilidade de o vampiro 1 vencer o combate.

Entrada
A entrada consiste de vários casos de teste. Cada caso de teste consiste de uma única linha, contendo 4 inteiros EV1, EV2, AT e D separados por espaços (1 ≤ EV1, EV2 ≤ 10, 1 ≤ AT ≤ 5 and 1 ≤ D ≤ 10). O final da entrada é indicado por uma linha contendo quatro zeros, separados por espaços.

Saída
Para cada caso de teste da entrada seu programa deve imprimir uma única linha. A linha deve conter apenas um número real, escrito com precisão de uma casa decimal, representando, em termos de percentagem, a probabilidade de o vampiro 1 vencer o combate. '''



v1 
v2 