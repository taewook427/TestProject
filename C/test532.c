#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void) {

	struct person {
		int height;
		float sight;
		char* name;
	};
	struct person bk;
	bk.height = 190;
	bk.sight = 0.01;
	bk.name = "DSBK";
	printf("Ű : %d, �÷� : %f, �̸� : %s\n", bk.height, bk.sight, bk.name);

	typedef struct {
		struct person baset;
		int workid;
	} teacher;
	teacher dolkong;
	dolkong.baset.height = 100;
	dolkong.baset.sight = 1.8;
	dolkong.baset.name = "DolKong";
	dolkong.workid = 500;
	printf("Ű : %d, �÷� : %f, �̸� : %s, ���̵� : %d\n", dolkong.baset.height, dolkong.baset.sight, dolkong.baset.name, dolkong.workid);

	struct person* mylove0 = &bk;
	mylove0->height = 250;
	printf("Ű : %d, �÷� : %f, �̸� : %s\n", bk.height, bk.sight, bk.name);
	teacher* mylove1 = &dolkong;
	mylove1->baset.sight = 23.0;
	printf("Ű : %d, �÷� : %f, �̸� : %s, ���̵� : %d\n", dolkong.baset.height, dolkong.baset.sight, dolkong.baset.name, dolkong.workid);

	teacher people[5];
	for (int i = 0; i < 5; i++) {
		people[i].workid = i * 100;
		people[i].baset.height = 160 + i * 6;
		people[i].baset.sight = 1.0 - 0.1 * i;
		people[i].baset.name = "DSlove";
	}
	for (int i = 0; i < 5; i++) {
		printf("Ű : %d, �÷� : %f, �̸� : %s, ���̵� : %d\n",
			people[i].baset.height,
			people[i].baset.sight,
			people[i].baset.name,
			people[i].workid);
	}

	return 0;
}