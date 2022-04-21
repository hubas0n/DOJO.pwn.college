#include <stdio.h>

void pwncollege(){

}

int fork();
int execve();
int wait();

int main(){
        if(fork()==0)
                execve("/challenge/embryoio_level29",NULL,NULL);
        else
                wait(NULL);
        return 0;
}
