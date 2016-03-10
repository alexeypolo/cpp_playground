#include <stdio.h>

#define PL_SIZE 6
const int pl_stages[PL_SIZE] = {100, 101, 102, 103, 104, 105};
int pl_index_of_zero_stage = 0;
int cycle = 0;

int pl_stage2index(int stage) {
    return (pl_index_of_zero_stage + stage) % PL_SIZE;
}

void pl_step() {
    pl_index_of_zero_stage = (pl_index_of_zero_stage + PL_SIZE - 1) % PL_SIZE;
}

void pl_dump() {
    int stage;

    printf("C.%d: dump\n", cycle);
    for (int stage = 0; stage < PL_SIZE; stage++) {
        int index = pl_stage2index(stage);
        printf("stage %d, index %d, record_id %d\n", stage, index, pl_stages[index]);
    }
}

void simulate_cycle() {
    pl_dump();
    pl_step();
}

int main() {
    do {
      simulate_cycle();
    } while(++cycle < 10);

    return 0;
}
