#include <stdio.h>

void inBoi7HaiChuSo() {
  int i;
  for (i = 10; i <= 98; i++) {
    if (i % 7 == 0) {
      printf("%d ", i);
    }
  }
}

int main() {
    printf("Cac so hai chu so la boi cua 7: ");
  inBoi7HaiChuSo();
  return 0;
}
