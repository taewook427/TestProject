#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int med3(int a, int b, int c) {
	if ( (a >= b && b >= c) || (c >= b && b >= a) ) {
		return b;
	}
	else if ((a >= c && c >= b) || (b >= c && c >= a)) {
		return c;
	}
	else {
		return a;
	}
}

int main(void) {
	int a, b, c;

	printf("�� ������ �߾Ӱ��� ���մϴ�.\n");
	printf("a �Է� : ");  scanf("%d", &a);
	printf("b �Է� : ");  scanf("%d", &b);
	printf("c �Է� : ");  scanf("%d", &c);

	printf( "%d\n", med3(a, b, c) );

	a = 17;
	b = 27;
	int min = a < b ? a : b; // 3�� ������
	printf("%d\n", min);
	a = 37;
	b = 27;
	min = a < b ? a : b;
	printf("%d\n", min);
}