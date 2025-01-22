# Demonstrator Source
# Print a message from Module A to the Console
# Print a message from Module B to the Console

// demonstrator.c
#include <stdio.h>
#include "module_a.h"
#include "module_b.h"

int main() {
    hello_a();
    hello_b();
    return 0;
}