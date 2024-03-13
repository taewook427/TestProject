#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int guarded_linear_search(int* arr, int length, int key) { // �迭 ������ �� ĭ�� ������ƾ� ��
	int temp = 0;
	arr[length] = key;
	while (1) {
		if (arr[temp] == key) {
			break;
		} // ���ʹ��� �� Ƚ���� ������ �ȴ�
		temp++;
	}
	return temp == length ? -1 : temp;
}

int linear_search(int* arr, int length, int key) {
	int temp = 0;
	int flag = 1;
	while (flag) {
		if (temp == length) {
			flag = 0;
			temp = -1;
		}
		else {
			if (arr[temp] == key) {
				flag = 0;
			}
			else {
				temp++;
			}
		}
	}
	return temp;
}

int binary_search(int* arr, int length, int key) {
	int start = 0;
	int end = length;
	int current = length / 2;
	if (length == 0) { return -1; }
	else {
		while (start <= end) {
			current = (start + end) / 2;
			if (arr[current] < key) {
				start = current + 1;
			}
			else if (arr[current] > key) {
				end = current - 1;
			}
            else {
				return current;
			}
		}
		return -1;
	}
}

// char�� �빮��ȭ �� �� ���ϴ� �Լ�
int check(const char* a, const char* b) {
	int aa = *a;
	int bb = *b;
	if (aa <= 'Z') {
		aa += 32;
	}
	if (bb <= 'Z') {
		bb += 32;
	}
	return aa < bb ? -1 : aa > bb ? 1 : 0; // ������ ����, ������ 0, ũ�� ���
}

int sum(int a, int b) {
	return a + b;
}
int sub(int a, int b) {
	return a - b;
}
int mul(int a, int b) {
	return a * b;
}
void draw(int(*fp)(int, int)) {
	for (int i = 1; i < 10; i++) {
		for (int j = 1; j < 10; j++) {
			printf("%3d", (*fp)(i, j));
		}
		putchar('\n');
	}
}

int main(void) {
	int base0[10] = {5, 13, -1, 8, -2, 27, 13, -7, -8, 0};
	for (int i = 0; i < 10; i++) { printf("%d, ", base0[i]); }
	printf("\nlinear_search\n");
	printf("-8 : %d\n", linear_search(base0, 10, -8));
	printf("6 : %d\n", linear_search(base0, 10, 6));

	int base1[11] = {4, 7, 1, 9, -5, -25, 3, 34, -1, -5, 0};
	for (int i = 0; i < 10; i++) { printf("%d, ", base1[i]); }
	printf("\nguarded_linear_search\n");
	printf("-1 : %d\n", guarded_linear_search(base1, 10, -1));
	printf("10 : %d\n", guarded_linear_search(base1, 10, 10));

	int base2[17] = {-16, -8, -4, -1, 0, 1, 2, 4, 7, 8, 9, 10, 13, 17, 34, 56, 1080};
	for (int i = 0; i < 17; i++) { printf("%d, ", base2[i]); }
	printf("\nbinary_search\n");
	printf("-90 : %d\n", binary_search(base2, 17, -90));
	printf("-16 : %d\n", binary_search(base2, 17, -16));
	printf("-1 : %d\n", binary_search(base2, 17, -1));
	printf("17 : %d\n", binary_search(base2, 17, 17));
	printf("1080 : %d\n", binary_search(base2, 17, 1080));
	printf("2160 : %d\n", binary_search(base2, 17, 2160));

	char base3[15] = {'a', 'b', 'C', 'e', 'F', 'H', 'i', 'k', 'm', 'N', 'o', 'q', 'R', 'S', 'w'};
	char key;
	int* loc; 
	for (int i = 0; i < 15; i++) { printf("%c, ", base3[i]); }
	printf("\nstdlib.bsearch\n");
	/* bsearch�� Ű�� ������, Ÿ�� �迭, �迭 ũ��, ���� ũ��, ���Լ��� �޾�
	Ű�� ������ Ű���� ���� ������, ������ �� �����͸� ��ȯ�Ѵ�.
	�迭�� ���ĵ� ���¿��� �ϸ�, 
	���� ���� �������� ���� ���� �ƹ��ų��� ��ġ�� ��ȯ�Ѵ�. */
	key = 'a';
	loc = bsearch(&key, base3, 15, sizeof(char), (int(*) (const void*, const void*)) check);
	if (loc == NULL) {
		printf("a : -1\n");
	}
	else {
		printf("a : %d\n", (int)loc - (int)base3);
	}
	key = 'c';
	loc = bsearch(&key, base3, 15, sizeof(char), (int(*) (const void*, const void*)) check);
	if (loc == NULL) {
		printf("c : -1\n");
	}
	else {
		printf("c : %d\n", (int)loc - (int)base3);
	}
	key = 'N';
	loc = bsearch(&key, base3, 15, sizeof(char), (int(*) (const void*, const void*)) check);
	if (loc == NULL) {
		printf("N : -1\n");
	}
	else {
		printf("N : %d\n", (int)loc - (int)base3);
	}
	key = 'z';
	loc = bsearch(&key, base3, 15, sizeof(char), (int(*) (const void*, const void*)) check);
	if (loc == NULL) {
		printf("z : -1\n");
	}
	else {
		printf("z : %d\n", (int)loc - (int)base3);
	}
	// �� �Լ��� bsearch�� void���� �ִ� Ÿ�� ������ �� ���̰�,
	// �� �Լ��� void*�� ������ ��ȯ�� �ʿ�� ����.

	/* double func(int) : int�� �޾� double�� ��ȯ�ϴ� �Լ�
	double (*funcptr) (int) : int�� �޾� double�� ��ȯ�ϴ� �Լ��� ���� ������*/
	draw(sum);
	draw(sub);
	draw(mul);

	char name0[20] = "�躴��";
	char name1[20] = "�赹��";
	char name2[20] = "DongSung";
	printf("%s vs %s : %d\n", name0, name1, strcmp(name0, name1));
	printf("%s vs %s : %d\n", name1, name2, strcmp(name2, name0));
	printf("%s vs %s : %d\n", name0, name0, strcmp(name0, name0));
	// ���ڿ� �� �Լ�, ũ�� ���, ������ ����, ������ 0 ��ȯ

	return 0;
}