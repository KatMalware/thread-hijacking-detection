#define _GNU_SOURCE
#include <sched.h>
#include <unistd.h>

int child() { return 0; }

int main() {
    clone(child, 0, CLONE_VM|CLONE_FS|CLONE_FILES, 0);
}
