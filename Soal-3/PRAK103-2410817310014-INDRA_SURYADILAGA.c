#include <stdio.h>

int main() {
    float a = 5;
    float b = 6;
    float x = 7;
    float y = 8;
    
    printf("Variabel a bernilai %.0f\n",a);
    printf("Variabel b bernilai %.0f\n",b);
    printf("Variabel x bernilai %.0f\n",x);
    printf("Variabel y bernilai %.0f\n",y);
    printf("Jumlah a ditambah b dikali x dibagi y adalah %.4f\n", a+b*x/y);
    return 0;
}