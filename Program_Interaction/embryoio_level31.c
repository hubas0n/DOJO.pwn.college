#include <stdio.h>
void pwncollege(){
}
int fork();
int execve();
int wait();
int main(int argc, char *argv[]){
    argv[1]="whatever";
    if(fork()==0) 
      execve("/challenge/embryoio_level31",argv,NULL);
    else
      wait(NULL);
  return 0;
}
