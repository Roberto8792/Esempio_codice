#include <stdio.h> 
#define USE_MATH_DEFINES
#include <math.h>

int main() {

    float D;

    printf("Inserisci un numero: ");
    scanf("%f", &D);
    
    printf("Questa è l'area del quadrato: %.2f\n", D * D);
    printf("Questa è l'area del triangolo: %.2f\n", sqrt(3)/4 * D * D);
    printf("Questa è l'area del cerchio: %.2f\n", D * D / 4 * M_PI);

}

