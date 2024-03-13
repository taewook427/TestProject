#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include "test512.h"

// �ʱ�ȭ ������ 0 ���н� -1
int SInit(Stk* s, int max) {
	s->ptr = 0;
	s->stk = calloc(max, sizeof(int));
	if (s->stk == NULL) {
		s->max = 0;
		return -1;
	}
	s->max = max;
	return 0;
}

// Ǫ�� ������ 0 ���н� -1
int SPush(Stk* s, int x) {
	if (s->ptr >= s->max) {
		return -1;
	}
	else {
		s->stk[s->ptr] = x;
		s->ptr++;
		return 0;
	}
}

// �� ������ 0 ���н� -1
int SPop(Stk* s, int* x) {
	if (s->ptr <= 0) {
		return -1;
	}
	else {
		*x = s->stk[s->ptr - 1];
		s->ptr--;
		return 0;
	}
}

// �� ������ 0 ���н� -1
int SPeek(const Stk* s, int* x) {
	if (s->ptr <= 0) {
		return -1;
	}
	else {
		*x = s->stk[s->ptr - 1];
		return 0;
	}
}

// ���� ����
void SClear(Stk* s) {
	s->ptr = 0;
}

// ���� �ִ� �뷮 ���ϱ�
int SCap(const Stk* s) {
	return s->max;
}

// ���� ������ �� ���ϱ�
int SSize(const Stk* s) {
	return s->ptr;
}

// ��������� 1, �ƴϸ� 0
int SIsEmpty(const Stk* s) {
	return s->ptr <= 0;
}

// ���� ���� 1, �ƴϸ� 0
int SIsFull(const Stk* s) {
	return s->ptr >= s->max;
}

// ������ �� �˻�
int SSch(const Stk* s, int x) {
	int i;
	for (i = s-> ptr - 1; i >= 0; i--) {
		if (s->stk[i] == x) {
			return i;
		}
	}
	return -1;
}

// �ٴ� -> ����� ������ ���
void SPrint(const Stk* s) {
	int i;
	for (i = 0; i < s->ptr; i++) {
		printf( "%d ", s->stk[i] );
	}
	printf("\n");
}

// ���� ����
void STer(Stk* s) {
	if (s->stk != NULL) {
		free(s->stk);
	}
	s->max = 0;
	s->ptr = 0;
}

// �ʱ�ȭ ������ 0 ���н� -1
int QInit(Quu* q, int max) {
	q->ptr = 0;
	q->size = 0;
	q->quu = calloc(max, sizeof(int));
	if (q->quu == NULL) {
		q->max = 0;
		return -1;
	}
	else {
		q->max = max;
		return 0;
	}
}

// �ֱ� ������ 0 ���н� -1
int QEnq(Quu* q, int x) {
	if (q->size < q->max) {
		q->quu[(q->ptr + q->size) % q->max] = x;
		q->size = q->size + 1;
		return 0;
	}
	else {
		return -1;
	}
}

// ���� ������ 0 ���н� -1
int QDeq(Quu* q, int* x) {
	if (q->size <= 0) {
		return -1;
	}
	else {
		*x = q->quu[q->ptr];
		q->size = q->size - 1;
		q->ptr = (q->ptr + 1) % q->max;
		return 0;
	}
}

// ������ �� �˻�
int QSch(const Quu* q, int x) {
	int i = 0;
	for (i = 0; i < q->size; i++) {
		if (q->quu[(q->ptr + i) % q->max] == x) {
			return (q->ptr + i) % q->max;
		}
	}
	return -1;
}

// ��� ������ ���
void QPrint(const Quu* q) {
	int i = 0;
	for (i = 0; i < q->size; i++) {
		printf("%d ", q->quu[(q->ptr + i) % q->max]);
	}
	printf("\n");
}

// ť ����
void QTer(Quu* q) {
	q->max = 0;
	q->ptr = 0;
	q->size = 0;
	if (q->quu != NULL) {
		free(q->quu);
	}
}