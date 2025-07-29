#include <stdio.h>

int main() {
  
    int primo_numero;
    int secondo_numero;
    int somma;

    printf("\nInserisci il primo numero: ");
    scanf("%d", &primo_numero);
    printf("\nInserisci il secondo numero: ");
    scanf("%d", &secondo_numero);
    
    somma = primo_numero + secondo_numero;
    printf("\nLa somma di %d + %d è = %d", primo_numero, secondo_numero, somma);
    return 0;
    
}
