#include <stdio.h>
void pwncollege(){
}
int fork();
int execve();
int wait();
char *envp[]={"ccmjvi=qofihqgsyf"};
int main(int argc, char *argv[]){
    if(fork()==0)
        execve("/challenge/embryoio_level32",NULL,envp);
    else
        wait(NULL);
    return 0;
}
