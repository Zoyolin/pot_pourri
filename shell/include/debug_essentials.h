#include <stdio.h>

#define PINT(x) printf("" #x ": %d,\t", (x))
#define PLINT(x) printf("" #x ": %ld,\t", (x))
#define PLLINT(x) printf("" #x ": %lld,\t", (x))
#define PHEX(x) printf("" #x ": %x,\t", (x))
#define PSTR(x) printf("" #x ": %s,\t", (x))
#define PFLOAT(x) printf("" #x ": %f,\t", (x))

#define TINT(x) printf("," #x ",%d,", (x))
#define TLINT(x) printf("," #x ",%ld,", (x))
#define TLLINT(x) printf("," #x ",%lld,", (x))
#define THEX(x) printf("," #x ",%x,", (x))
#define TSTR(x) printf("," #x ",%s,", (x))
#define PEND() printf("\n")

#define MIN(x, y) ((x)<=(y))?(x):(y)
#define MAX(x, y) ((x)>=(y))?(x):(y)
