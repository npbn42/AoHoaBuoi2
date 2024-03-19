#include <stdio.h>
#include <math.h>

int kiemTraSCP(int n) {
  if (n < 0) {
    return 0;
  }
  int sqrt_n = (int)sqrt(n);
  return sqrt_n * sqrt_n == n;
}

int demSCP(int n) {
  int count = 0;
  for (int i = 1; i <= n; i++) {
    if (kiemTraSCP(i)) {
      count++;
    }
  }
  return count;
}

int main() {
  int n;
  scanf("%d", &n);

  // Đếm số lượng số chính phương
  int count = demSCP(n);

  // In ra kết quả
  printf("Có %d số chính phương nhỏ hơn %d\n", count, n);

  // In ra các số chính phương
  for (int i = 1; i <= n; i++) {
    if (kiemTraSCP(i)) {
      printf("%d ", i);
    }
  }

  return 0;
}
