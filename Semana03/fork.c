#include <studio.h>
#include <sys/types.h>
#include <unistd.h>

inta main ()
{
	pid_t child_pid;
	printf(" The main program process ID is %d\n", (int) getpid();

	child_pid = fork ();
	if (child_pid != 0) {
		printf("this is the parent process, with id %d\n" (int) getpid ());
		printf("this child's process ID is %d\n", (int) child_pid);
}
else
	printf ("this is the child process, with id %d\n", (int getpid ());

return 0;
}