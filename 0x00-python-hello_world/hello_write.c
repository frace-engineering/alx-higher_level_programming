#include <unistd.h>
#include <stdio.h>
#include <string.h>



void hello_write(void)
{
	write(2, "and that piece of art is useful - Dora Korpar, 2015-10-19", 59);
	printf("\n");
}
