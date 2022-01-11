#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>


int main()
{
	char s1[20] = "12345";
	char s2[10] = "Pedro";
	char s3[10] = "PedroJacob";
	long int res;


	res = pow(9, 3);
	printf("Usando math.h, " 
	       "O valor é: %ld\n",res);

	long int a = atol(s1);
	printf("Usando stdlib.h, a string");
	printf("para long int: %ld\n", a);

	strcpy(s2, s3);
	printf("Usando string.h, as strings"
		"s2 e s3: %s %s\n",
		s2, s3);

	return 0;

}


