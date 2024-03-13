#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
// �Լ� ���� ��ũ��, do while�� ����, ��ũ�δ� �� �״�� ���ڿ��� ġȯ�� �Ѵ�!
# define swap(type, x, y) do {type t = x; x = y; y = t;} while(0)

void maxof(const int arr[], int size) { // const int* arr�� ����
	int n = sizeof(arr) / sizeof(int); // sizeof(arr)�� ������ ũ�⸸�� ��ȯ�� �ȵ�!
	int max = 0;
	for (int i = 0; i < size; i++) {
		if (arr[i] > max) {
			max = arr[i];
		}
	}
	printf("max = %d\n", max);
}

void rev(int* arr, int size) {
	for (int i = 0; i < size / 2; i++) {
		swap( int, arr[i], arr[size - i - 1] );
	}
}

int conv(unsigned x, int n, char d[]) {
	char dchar[] = "0123456789ABCDEF";
	int digits = 0;
	if (x == 0) {
		d[digits++] = dchar[0]; // �������������ڴ� �� ��ü�� ���ϰ� ������Ų��.
	}
	else {
		while (x) {
			d[digits++] = dchar[x % n];
			x /= n;
		}
	}
	return digits;
}

int main(void) {
	printf("�⺻ ���� : %d\n", rand());

	int n = 0;
	printf("�迭�� ���� : ");
	scanf("%d", &n);
	int* mem = malloc( n * sizeof(int) );

	srand( time(NULL) ); // time���� ���� �ʱ�ȭ
	for (int i = 0; i < n; i++) {
		mem[i] = 160 + rand() % 30; //rand�� ���� 0 ~ MAX_RAND=32767 ����
		printf("Ű %d = %d\n", i, mem[i]);
	}

	maxof(mem, n);
	rev(mem, n);
	for (int i = 0; i < n; i++) {
		printf("%d ", mem[i]);
	}
	printf("= rev\n");
	free(mem);

	// 0x1C hex, 034 oct
	int tgt = 12345678;
	char after[32];
	int digits = conv(tgt, 2, after);
	for (int i = 0; i < digits; i++) {
		printf("%c", after[digits - i - 1]);
	}
	printf(" = bin\n");
	digits = conv(tgt, 8, after);
	for (int i = 0; i < digits; i++) {
		printf("%c", after[digits - i - 1]);
	}
	printf(" = oct\n");
	digits = conv(tgt, 10, after);
	for (int i = 0; i < digits; i++) {
		printf("%c", after[digits - i - 1]);
	}
	printf(" = dec\n");
	digits = conv(tgt, 16, after);
	for (int i = 0; i < digits; i++) {
		printf("%c", after[digits - i - 1]);
	}
	printf(" = hex\n");

	printf("�� ��° �Ҽ����� ã����� : ");
	scanf("%d", &n);
	int* primes = malloc( n * sizeof(int) );
	if (n == 1) {
		printf("2\n");
	}
	else if (n == 2) {
		printf("2\n3\n");
	}
	else {
		primes[0] = 2;
		primes[1] = 3;
		tgt = 5;
		int add = 2;
		int num = 2;
		while (num != n) {
			int flag = 1;
			int current = 0;
			while (flag) {
				if (primes[current] * primes[current] > tgt) {
					flag = 0;
					primes[num] = tgt;
					num++;
					tgt = tgt + add;
					add = (add + 1) % 4 + 1;
				}
				else if (tgt % primes[current] == 0) {
					flag = 0;
					tgt = tgt + add;
					add = (add + 1) % 4 + 1;
				}
				current++;
			}
		}
		for (int i = 0; i < n; i++) {
			printf("%d\n", primes[i]);
		}
	}
	free(primes);

	// int[2][3] -> (0,0), (0,1), (0,2), (1,0), (2,1), (3,2)
	int low = 3;
	int col = 4;
	int marr[3][4] = { {0, 1, 2, 3}, {1, 2, 3, 4}, {2, 3, 4, 5} };
	for (int i = 0; i < low; i++) {
		for (int j = 0; j < col; j++) {
			printf("%d ", marr[i][j]);
		}
		printf("\n");
	}

	marr[1][1] = 10;
	marr[1][2] = 11;
	marr[2][1] = 12;
	marr[2][2] = 13;
	for (int i = 0; i < low; i++) {
		for (int j = 0; j < col; j++) {
			printf("%d ", marr[i][j]);
		}
		printf("\n");
	}

	int mmarr[3][4] = {0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2};
	for (int i = 0; i < low; i++) {
		for (int j = 0; j < col; j++) {
			printf("%d ", mmarr[i][j]);
		}
		printf("\n");
	}

	// int m[2][3] = { {1, 2, 0}, {4, 0, 0} };
	// int m[2][3] = {1, 2, 0, 4, 0, 0};
	// int m[2][3] = { {1, 2}, {4} }; -> ��� ����
	return 0;
}