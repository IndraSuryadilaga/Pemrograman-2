#include <stdio.h>

int main() {
    int putaran = 5;
    float jarak = 14.0;
    
    // Rumus untuk menghitung jari-jari
    float jarijari = jarak / (2 * 3.14159 * putaran);
    
    printf("Diketahui:\n");
    printf("Pak dengklek mengelilingi taman = %d Putaran\n", putaran);
    printf("Jarak tempuh Pak dengklek = %.0f Kilometer\n\n", jarak);
    printf("Jawab :\n");
    printf("Jari-jari taman yang dikelilingi Pak Dengklek adalah %.2f Kilometer\n", jarijari);
    
    return 0;
}