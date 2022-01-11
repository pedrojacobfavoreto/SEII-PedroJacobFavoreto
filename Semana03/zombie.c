#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
	pid_t child_pid;
	
	child_pid = fork ();
	if (child_pid > 0) {
	sleep;
	}
	else {
	exit (0);
	}
	return 0;
}
