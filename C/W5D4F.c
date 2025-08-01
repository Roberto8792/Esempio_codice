#include <stdio.h> 
#include <math.h>

double area_quadrato(double);

int main(){

    float D;
    float D1, D2, D3;

    printf("Inserisci tre numeri: ");
    scanf("%f %f %f", &D1, &D2, &D3);

    D = (D1 + D2 + D3) / 3;
    
    printf("Questa è l'area del quadrato: %.0f %.2f\n", area_quadrato(D), area_quadrato(D));
    printf("Questa è l'area del triangolo: %.0f %.2f\n", sqrt(3)/4 * D * D, sqrt(3)/4 * D * D);
    printf("Questa è l'area del cerchio: %.0f %.2f\n", D * D / 4 * M_PI, D * D / 4 * M_PI);

}
double area_quadrato(double lato){
    return lato * lato;
}
