#include <stdio.h>
#include <ctype.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>




#define DEFAULT_NAME "---indefinito---"


int partita();


int main() {
        // Introduzione al gioco
        char *intro = "\nCaro utente, un caloroso benvento al nostro quiz!"
                    "\nEcco a te una spiegazione del gioco di cui sarai partecipe. Il gioco consiste nel rispondere correttamente ad alcune domande che ti farò."
                    "\n\nAd ogni risposta corretta, riceverai un punto."
                    "\nSaranno domande a risposta multipla, quindi dovrai scegliere tra le opzioni fornite."
                    "\n\nAlla fine del quiz, il tuo punteggio totale sarà mostrato."
                    "\n\nBuona fortuna e che vinca il migliore!\n";
                    
    printf("%s", intro);

    char *prompt_scelta = "\n\nIniziamo il quiz!\nSei pronto? (S/N): ";
    printf("%s", prompt_scelta);
    
    char scelta;
    printf("\nInserisci qui la tua scelta: ");
    scanf(" %c", &scelta);


    int score = 0;
    char *nome = DEFAULT_NAME;

    printf("%c\n", scelta);

    switch (tolower(scelta)) {
        case 's':
            if(strcmp(nome, DEFAULT_NAME) == 0) {
                printf("\nPer favore, inserisci il tuo nome: ");
                nome = malloc(512);
                scanf("%s", nome);
                printf("\nBenvenuto %s! Sei pronto per iniziare il quiz?\n", nome);
               
            }
            
            printf("\nIl tuo punteggio iniziale è: %d\n", score);
            
            score += partita();
            printf("\nComplimenti!!! il quiz è terminato.");
            printf("\nIl tuo punteggio finale è: %d\n", score);
            break;
        case 'n':
            printf("\nVa bene, forse un'altra volta allora. Arrivederci!\n");
            break;
            return 0;
        default:
            printf("\nScelta non valida. Per favore, rispondi con S o N.\n");
            break;
            return 0;
    }
    }

int partita() {
    int score = 0;

    char *d1 = " Qual è la capitale d'Italia? \n\t1) Roma\n\t2) Poggibonsi\n\t3) Bassano del Grappa\n";
    int r1 = 1;
    int scelta;

    bool stop = false;
    while (!stop) {
        printf("%s\nRisposta: ", d1);
        scanf("%d", &scelta);
        switch(scelta) {
            case 1:
                printf("\nRisposta corretta!\n");
                score += 1;
                stop = true;
                break;
            default:
            case 2: case 3:
                printf("\nRisposta sbagliata. La risposta corretta era: %d\n", r1);
                score += 0;
                stop = true;
                break;
                printf("\nScelta non valida.\n");
    }
        }

    char *d2 = " Qual è l'unita di misura digitale? \n\t1) Centimetro\n\t2) Litro\n\t3) Byte\n";
    int r2 = 3;
    int scelta2;

    bool fermo = false;
    while (!fermo) {
        printf("%s\nRisposta: ", d2);
        scanf("%d", &scelta2);
        switch(scelta2) {
            case 3:
                printf("\nRisposta corretta!\n");
                score += 1;
                fermo = true;
                break;
            case 1: case 2:
                printf("\nRisposta sbagliata. La risposta corretta era: %d\n", r2);
                score += 0;
                fermo = true;
                break;
            default:
                printf("\nScelta non valida.\n");
    }
        }

        char *d3 = " Qual è la prima squadra di Roma? \n\t1) Lodigiani\n\t2) Lazio\n\t3) Roma\n";
    int r3 = 3;
    int scelta3;

    bool not = false;
    while (!not) {
        printf("%s\nRisposta: ", d3);
        scanf("%d", &scelta3);
        switch(scelta3) {
            case 3:
                printf("\nRisposta corretta!\n");
                score += 1;
                not = true;
                break;
            case 1: case 2:
                printf("\nRisposta sbagliata. La risposta corretta era: %d\n", r3);
                score += 0;
                not = true;
                break;
            default:
                printf("\nScelta non valida.\n");
    }
        }
    return score;
}
