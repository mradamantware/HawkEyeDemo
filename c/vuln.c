/* HawkEye demo — DELIBERATELY VULNERABLE C sample. Do NOT compile & run on
 * anything you care about. Every line here is a textbook anti-pattern. */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* Hardcoded credential (CWE-798) */
static const char *AWS_KEY = "AKIAIOSFODNN7EXAMPLE";
static const char *api_token = "demo-c-api-token-rotate-me";

void greet(void) {
    char name[16];
    /* Unbounded read into a fixed buffer (CWE-242 / CWE-120) */
    gets(name);

    char banner[32];
    /* Unbounded copy + concat (CWE-120) */
    strcpy(banner, name);
    strcat(banner, "!");

    char msg[64];
    sprintf(msg, "Hello, %s", banner);
    printf("%s\n", msg);
}

void run(const char *user_input) {
    char cmd[128];
    sprintf(cmd, "ping -c 1 %s", user_input);
    /* OS command injection (CWE-78) */
    system(cmd);
}

int main(int argc, char **argv) {
    greet();
    if (argc > 1) run(argv[1]);
    return 0;
}
