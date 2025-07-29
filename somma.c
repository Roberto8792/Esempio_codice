#include <stdio.h>

int main() {
  
    int primo_numero;
    int secondo_numero;
    int somma;

    printf("Inserisci il primo numero: ");
    scanf("%d", &primo_numero);
    printf("Inserisci il secondo numero: ");
    scanf("%d", &secondo_numero);
    
    somma = primo_numero + secondo_numero;
    printf("La somma dei due numeri è: %d\n", somma);
    return 0;
    
}
