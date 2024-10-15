#include <stdio.h>

int main() {
    float sepA = 100000;
    float sepB = 200000;
    float dis1 = 15;
    float dis2 = 70;
    
    printf("Harga sepatu A adalah %.0f\n",sepA);
    printf("Harga sepatu B adalah %.0f\n",sepB);
    printf("Harga sepatu A setelah diskon %.0f%% adalah %.0f \n", dis1, sepA-(sepA*dis1/100));
    printf("Harga sepatu B setelah diskon %.0f%% adalah %.0f \n", dis2, sepB-(sepB*dis2/100));
    return 0;
}