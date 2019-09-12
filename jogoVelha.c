#include <stdio.h>

char peca(int i) {
    switch(i) {
        case 1:
            return 'X';
        case 0:
            return ' ';
        case 2:
            return 'O';
    }
}

void desenha(int b[9]) {
    printf(" %c | %c | %c\n",peca(b[0]),peca(b[1]),peca(b[2]));
    printf("---+---+---\n");
    printf(" %c | %c | %c\n",peca(b[3]),peca(b[4]),peca(b[5]));
    printf("---+---+---\n");
    printf(" %c | %c | %c\n",peca(b[6]),peca(b[7]),peca(b[8]));
}

int win(const int tabuleiro[9]) {
    unsigned wins[8][3] = {{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}};
    int i;
    for(i = 0; i < 8; ++i) {
        if(tabuleiro[wins[i][0]] != 0 &&
           tabuleiro[wins[i][0]] == tabuleiro[wins[i][1]] &&
           tabuleiro[wins[i][0]] == tabuleiro[wins[i][2]])
            return tabuleiro[wins[i][2]];
    }
    return 0;
}

void joga(int tabuleiro[9], int jogador) {
    int posicao = 0, oponente;
    if(jogador == 1)
        oponente = 2;
    else
        oponente = 1;
    do {
        printf("\nJogador %d insira posicao de 1 a 9: ", jogador);
        scanf("%d", &posicao);
        posicao --;
        printf("\n");
    } while (posicao >= 9 || posicao < 0 && tabuleiro[posicao] == 0 || tabuleiro[posicao] == oponente );
    tabuleiro[posicao] = jogador;
}

int main() {
    int tabuleiro[9] = {0,0,0,0,0,0,0,0,0};
    printf("Jogador 1: O, Jogador 2: X\n");
    unsigned vez;
    int jogador;
    for(vez = 0; vez < 9 && win(tabuleiro) == 0; ++vez) {
        if(vez % 2 == 0){
            jogador = 1;
            desenha(tabuleiro);
            joga(tabuleiro,jogador);
        }
        else {
            jogador = 2;
            desenha(tabuleiro);
            joga(tabuleiro,jogador);
        }
    }
    switch(win(tabuleiro)) {
        case 0:
            desenha(tabuleiro);
            printf("Velha\n");
            break;
        case 1:
            desenha(tabuleiro);
            printf("Jogador 1 venceu\n");
            break;
        case 2:
            desenha(tabuleiro);
            printf("Jogador 2 venceu\n");
            break;
    }
}
