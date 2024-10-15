#include <stdio.h>

int main() {
    int ZhongArmy = 958730;
    char *PowerRanger[] = {"Zilong", "Ling", "Baxia", "Wanwan", "Change"};
    int jumlahPahlawan = sizeof(PowerRanger) / sizeof(PowerRanger[0]);

    printf("Jumlah pasukan yang dibawa Yu Zhong adalah %d\n", ZhongArmy);
    printf("Jumlah pahlawan adalah %d\n", jumlahPahlawan);
    printf("Jumlah pasukan yang harus dikalahkan setiap pahlawan adalah %d pasukan\n", ZhongArmy / jumlahPahlawan);

    return 0;
}