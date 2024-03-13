#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

void maxof(const int arr[]) { // const int* arr�� ����
	int n = sizeof(arr) / sizeof(int); // �迭�� ������, const�� �б�����
	int max = 0;
	for (int i = 0; i < n; i++) {
		if (arr[i] > max) {
			max = arr[i];
		}
	}
	printf("%d\n", max);
}

int main(void) {
	int mem0[5];
	for (int i = 0; i < 5; i++) {
		printf("%d ��° �׸� : ", i);
		scanf("%d", &mem0[i]);
	}
	for (int i = 0; i < 5; i++) {
		printf("%d ��° �׸� : %d\n", i, mem0[i]);
	}

	int mem1[] = { 0, 0, 0, 0, 0 }; // int mem1[5] = { 0, 0, 0, 0, 0 };
	printf( "%d, %d\n", sizeof(mem1), sizeof(mem1[0]) );

	int* mem2 = calloc(3, sizeof(int)); // int�� 3��, 0���� �ʱ�ȭ
	int* mem3 = malloc(3 * sizeof(int)); // 12����Ʈ ����, �ʱ�ȭ ����
	if (mem2 == NULL) {
		puts("�޸� �Ҵ� ����"); // ����
	}
	if (mem3 == NULL) {
		puts("�޸� �Ҵ� ����");
	}
	mem3[0] = 0;
	mem3[1] = 0;
	mem3[2] = 0;
	for (int i = 0; i < 3; i++) {
		printf( "%d, %d, ", mem2[i], mem3[i] );
	}
	free(mem2); // �ʼ� !!!!!!!!!!
	free(mem3);

	printf("%d, ", mem3[0]); // �������� �Ǵµ� ������ ��

	int* x;
	int y = 1000;
	x = &y;
	*x = 999;
	printf("%d, ", y);

	mem2 = calloc( 5, sizeof(int) );
	mem2[4] = 2048;
	printf("%d, ", mem2 + 3);
	printf("%d, ", mem2 + 4);
	printf("%d, ", mem2 + 5); // C�� ���� �ʴ´�
	printf( "%d, ", *(mem2 + 4) );

	// 0�� ��� �����ͷ� ��ȯ ����, �� ��ü�� NULL ������
	mem2[0] = mem2;
	printf("%d\n", mem2[0]); // �����ʹ� 64��Ʈ ������ ���̴�.
	free(mem2);

	mem2 = malloc(12);
	mem2[0] = 168;
	mem2[1] = 183;
	mem2[2] = 174;
	mem3[0] = 256; // C�� ���� �ʴ´�
	maxof(mem2);
	free(mem2);

	return 0;
}