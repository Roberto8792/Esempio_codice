#include <stdio.h>

int main() {
  
    int primo_numero;
    int secondo_numero;

    printf("\nInserisci il primo valore: ");
    scanf("%d", &primo_numero);
    printf("\nInserisci il secondo valore: ");
    scanf("%d", &secondo_numero);
    
    if (primo_numero == secondo_numero) printf("\n%d e %d sono uguali", primo_numero, secondo_numero);
    if (primo_numero != secondo_numero) printf("\n%d e %d non sono uguali", primo_numero, secondo_numero);
    if (primo_numero < secondo_numero) printf("\n%d è minore di %d", primo_numero, secondo_numero);
    if (primo_numero > secondo_numero) printf("\n%d è maggiore di %d", primo_numero, secondo_numero);
    if (primo_numero <= secondo_numero) printf("\n%d è minore o uguale di %d", primo_numero, secondo_numero);
    if (primo_numero >= secondo_numero) printf("\n%d è maggiore o uguale di %d", primo_numero, secondo_numero);
    if (primo_numero % 2 == 0 && secondo_numero % 2 == 0) printf("\n%d e %d sono entrambi numeri pari", primo_numero, secondo_numero);
    if (primo_numero % 2 == 0 || secondo_numero % 2 == 0) printf("\nfra %d e %d c'è un numeri pari", primo_numero, secondo_numero);
    if (!primo_numero % 2 == 0 || secondo_numero % 2 == 0) printf("\n%d è un numeri dispari", primo_numero);

    return 0;
    
}
