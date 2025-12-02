#include <sys/mman.h>
#include <unistd.h>

int main(){
    void *p = mmap(0, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
    mprotect(p, 4096, PROT_READ|PROT_WRITE|PROT_EXEC);
    return 0;
}
