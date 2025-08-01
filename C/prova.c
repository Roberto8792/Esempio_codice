//includo tutte le librerie necessarie alla compilazione del programma
#include <stdio.h>
#include <ctype.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
// Definisco una costante per il nome di default
// Questa costante verrà utilizzata per inizializzare la variabile nome
// Se l'utente non inserisce un nome, verrà utilizzato questo valore
#define DEFAULT_NAME "---indefinito---"
// Dichiarazione della funzione partita che gestisce il quiz
int partita();
// Funzione principale del programma
int main() {
    // Dichiarazione delle variabili necessarie
    char scelta;
    int score;
    char *nome = DEFAULT_NAME;
    // Creo un'ntroduzione al gioco
    char *intro = "\nCaro utente, un caloroso benvento al nostro quiz!"
                  "\nEcco a te una spiegazione del gioco di cui sarai partecipe. Il gioco consiste nel rispondere correttamente ad alcune domande che ti farò."
                  "\n\nAd ogni risposta corretta, riceverai un punto."
                  "\nSaranno domande a risposta multipla, quindi dovrai scegliere tra le opzioni fornite."
                  "\n\nAlla fine del quiz, il tuo punteggio totale sarà mostrato."
                  "\n\nBuona fortuna e che vinca il migliore!\n";
    printf("%s", intro);
    // Chiedo all'utente se è pronto a iniziare il quiz
    do {
        printf("\n\nSei pronto a iniziare il quiz? (S/N): ");
        scanf(" %c", &scelta);
        // Converto la scelta in minuscolo con la strcmp (inclusa nella libreria string.h  ) per confrontare due variabili
        switch (tolower(scelta)) {
            // Se l'utente risponde 's' o 'S', inizio il quiz
            case 's':
                // Se il nome è quello di default, chiedo all'utente di inserire il suo nome
                if(strcmp(nome, DEFAULT_NAME) == 0) {
                    printf("\nPer favore, inserisci il tuo nome: ");
                    // Alloco memoria per il nome dell'utente
                    nome = malloc(512);
                    // Leggo il nome inserito dall'utente
                    scanf("%s", nome);
                    // Stampo un messaggio di benvenuto con il nome dell'utente
                    printf("\nBenvenuto %s! Iniziamo il quiz!\n", nome);
                }
                // Inizializzo il punteggio a 0
                score = 0;
                // Stampo il punteggio iniziale
                printf("\nIl tuo punteggio iniziale è: %d\n", score);
                // Aggiungo il punteggio ottenuto alla variabile score
                score += partita();
                printf("\nComplimenti!!! Il quiz è terminato.");
                // Mostro il punteggio finale
                printf("\nIl tuo punteggio finale è: %d\n", score);
                // Libero la memoria allocata per il nome
                break;
            // Se l'utente risponde 'n' o 'N', esco dal programma
            case 'n':
                printf("\nVa bene, forse un'altra volta allora. Arrivederci!\n");
                break;
            // Se l'utente risponde con un'altra lettera, mostro un messaggio di errore
            default:
                printf("\nScelta non valida. Per favore, rispondi con S o N.\n");
                break;
        }
    // Chiedo all'utente se vuole continuare a giocare
    } while (tolower(scelta) != 'n');
    // Se il nome non è quello di default, libero la memoria allocata
    
    if (nome != DEFAULT_NAME) {
    
        free(nome);
    }

    return 0;
}

int partita() {
    // Inizializzo il punteggio a 0
    // Questa variabile terrà traccia del punteggio dell'utente durante il quiz
    // Ogni risposta corretta incrementerà il punteggio di 1
    // Alla fine del quiz, il punteggio totale sarà mostrato all'utente
    int score = 0;
// Dichiarazione della domanda1 e della risposta corretta
    char *d1 = " Qual è la capitale d'Italia? \n\t1) Roma\n\t2) Poggibonsi\n\t3) Bassano del Grappa\n";
    int r1 = 1;
    int scelta;
// Variabile booleana per controllare il ciclo
    bool stop = false;
    // Inizio del ciclo per la domanda 1
    while (!stop) {
        printf("%s\nRisposta: ", d1);
        scanf("%d", &scelta);
        switch(scelta) {
            case 1:
                printf("\nRisposta corretta!\n");
                // Incremento il punteggio di 1 per la risposta corretta
                score += 1;
                // Imposto stop a true per uscire dal ciclo
                stop = true;
                break;
            default:
            // Se l'utente risponde con un'altra opzione, mostro un messaggio di errore
            case 2: case 3:
                printf("\nRisposta sbagliata. La risposta corretta era: %d\n", r1);
                stop = true;
                break;
        }
    }
// Dichiarazione della domanda2 e della risposta corretta
    char *d2 = " Qual è l'unita di misura digitale? \n\t1) Centimetro\n\t2) Litro\n\t3) Byte\n";
    int r2 = 3;
    int scelta2;
// Variabile booleana per controllare il ciclo
    // Inizio del ciclo per la domanda 2
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
                fermo = true;
                break;
            default:
                printf("\nScelta non valida.\n");
        }
    }
// Dichiarazione della domanda3 e della risposta corretta
    char *d3 = " Qual è la prima squadra di Roma? \n\t1) Lodigiani\n\t2) Lazio\n\t3) Roma\n";
    int r3 = 3;
    int scelta3;
// Variabile booleana per controllare il ciclo
// Inizio del ciclo per la domanda 3
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
                not = true;
                break;
            default:
                printf("\nScelta non valida.\n");
        }
    }
// Restituisco il punteggio totale ottenuto dall'utente
    return score;
}