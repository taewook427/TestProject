#ifndef ___IBset
#define ___IBset

typedef struct {
	int max;
	int num;
	int* set;
} Iset;

int Iinit(Iset* s, int max); // �ʱ�ȭ

int Imember(Iset* s, int n); // ����ΰ�?

void Iadd(Iset* s, int n); // �����߰�

void Iremove(Iset* s, int n); // ��������

int Icap(Iset* s); // �߰� ���� ���Ҽ�

int Isize(Iset* s); // ���Ҽ�

void Iassign(Iset* s0, Iset* s1); // ����, s0 = s1

int Iequal(Iset* s0, Iset* s1); // ��� Ȯ��

Iset* Iunion(Iset* s0, Iset* s1, Iset* s2); // s0 = s1 �� s2

Iset* Iinter(Iset* s0, Iset* s1, Iset* s2); // s0 = s1 �� s2

Iset* Idiffer(Iset* s0, Iset* s1, Iset* s2); // s0 = s1 - s2

void Iprint(Iset* s); // ���

void Iter(Iset* s); // ����

typedef unsigned long long Bset; // 0~63 ���� ����

#define Bnull (Bset)0 // ������
#define Bbits 64 // ��ȿ��Ʈ��
#define Bnum(n) ((Bset)1 << (n)) // ���� {n}

long long Bmember(Bset s, int n); // s�� n ����?

void Badd(Bset* s, int n); // s�� n �ֱ�

void Bremove(Bset* s, int n); // s���� n ����

int Bsize(Bset s); // s ũ��

void Bprint(Bset s); // s ���

#endif