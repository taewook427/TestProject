#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void tri(int n) {
	for (int i = 1; i < n + 1; i++) {
		for (int j = 1; j < i; j++) {
			putchar('*');
		}
		putchar('\n');
	}
}

int main(void) {
	int n = 0;
	printf("n�� 5�� ��� Ȥ�� 6�� ���\nn : ");
	scanf("%d", &n);
	if ( (n % 5 == 0) || (n % 2 == 0) && (n % 3 == 0) ) {
		puts("���ǿ� �½��ϴ�.");
	}

	for (int i = 1; i < 10; i++) {
		for (int j = 1; j < 10; j++) {
			printf("%3d ", i * j);
		}
		printf("\n");
	}

	printf("%d�� ���� �ﰢ��", n);
	tri(n);

	return 0;
}