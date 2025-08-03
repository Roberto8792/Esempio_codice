#include <stdio.h>
#include <ctype.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#define DEFAULT_NAME "---indefinito---"

int partita();
int domanda (char*,int);
bool contains (int*,int);

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
    char scelta;
    int score = 0;
    char nome[512] = DEFAULT_NAME;

    while (true) {
    printf("%s", prompt_scelta);
    printf("\nInserisci qui la tua scelta: ");
    scanf(" %c", &scelta);

    switch (tolower(scelta)) {
        case 's':
            if(strcmp(nome, DEFAULT_NAME) == 0) {
                printf("\nPer favore, inserisci il tuo nome: ");
                scanf("%s", nome);
                printf("\nBenvenuto %s! Sei pronto per iniziare il quiz?\n", nome);
               
            }
            score += partita();
            break;
        case 'n':
            printf("\nVa bene, forse un'altra volta allora. Arrivederci!\n");;
            return 0;
        default:
            printf("\nScelta non valida. Per favore, rispondi con S o N.\n");
            break;
    }
    }
}

int partita() {
    int score = 0;

    score += domanda( "Qual è la capitale d'Italia? \n\t1) Roma\n\t2) Poggibonsi\n\t3) Bassano del Grappa\n",
        1
    );

    score += domanda("Qual è l'unita di misura digitale? \n\t1) Centimetro\n\t2) Litro\n\t3) Byte\n",
        3
    );

    score += domanda("Qual è la prima squadra di Roma? \n\t1) Lodigiani\n\t2) Lazio\n\t3) Roma\n",
        3
    );
    return score;
}  
     
// controlla che l'elemento sia contenuto nell'array
// arr = [1, 2 ,3] | element = 3
bool contains(int *arr, int element) {
    for(int i=0; i<sizeof(arr); i++) {
        if(arr[i] == element) {
            return true;
        }
    }
    return false;
}

// generalizza il processo per il quiz
int domanda(char *d, int correct) {
    int scelta;
    int possible_answers[] = {1, 2, 3};

    while(true) {
        printf("%s\nRisposta: ", d);
        scanf("%d", &scelta);

        if(scelta == correct) {
            return 1;
        } else if(contains(possible_answers, scelta)) {
            return 0;
        } else {
            printf("Not an option\n");
        }
    }
}