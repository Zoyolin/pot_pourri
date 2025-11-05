/*Area51
	gcc  $(realpath $0) -o $(basename $0).run -Iinclude \
	&& $(dirname $(realpath $0))/$(basename $0).run
	exit
*/

#include "debug_essentials.h"
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PATH_LEN 1000
#define MAX_SHORTEN_LEN 100
#define CURRENT_DIR_CHAR_ALLOWANCE 12
int main(int argc, char* argv[])
{
	char* cwd = getcwd(NULL, 0);

	// PSTR(cwd);
	unsigned int len = strnlen(cwd, 1000000);
	char* scwd = malloc(MAX_SHORTEN_LEN + 1);
	char* write_p = scwd + MAX_SHORTEN_LEN;
	*write_p-- = 0;

	int depth_allowance = CURRENT_DIR_CHAR_ALLOWANCE;
	int word_len = 0;
	int i = len - 1;
	do
	{
		if(depth_allowance == CURRENT_DIR_CHAR_ALLOWANCE)
			*write_p-- = cwd[i];
		if (cwd[i] == '/')
		{
			if(depth_allowance != CURRENT_DIR_CHAR_ALLOWANCE)
			{
				int to_be_written =  MIN(word_len, depth_allowance); 
// PINT(to_be_written);
				if(write_p - to_be_written < scwd)
					break;
				int j = to_be_written;
				do{
					*write_p-- = cwd[i+j];
				}while(j--);
			}

			word_len = 0;
			depth_allowance /= 2;
			depth_allowance += 1;
// PSTR(write_p+1);
// PEND();
		}
		else
			word_len++;
	}while(i-- && (write_p > scwd));

	puts(write_p+1);

	free(cwd);
	free(scwd);
	return 0;
}

