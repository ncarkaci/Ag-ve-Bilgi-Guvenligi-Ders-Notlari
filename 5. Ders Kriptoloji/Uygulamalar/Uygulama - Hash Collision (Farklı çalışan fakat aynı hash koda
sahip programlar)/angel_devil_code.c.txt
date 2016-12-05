
#include <string.h>
#include <stdio.h>


#define DUMMY "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" \
 "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" \
 "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" \
 "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" \
 "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" \
 "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

int angel();
int devil();

char *dummya = DUMMY "A";
char *dummyb = DUMMY "B";

int main() {
  if (strcmp(dummya, dummyb) != 0) {
    return angel();
  } else {
    return devil();
  }
}


int angel() {
    fprintf(stdout, ".                                       ,\n");
    fprintf(stdout, ")).               -===-               ,((\n");
    fprintf(stdout, "))).                                 ,(((\n");
    fprintf(stdout, "))))).            .:::.           ,((((((\n");
    fprintf(stdout, "))))))))).        :. .:        ,(((((((('\n");
    fprintf(stdout, "`))))))))))).     : - :    ,((((((((((((\n");
    fprintf(stdout, "))))))))))))))))_:' ':_((((((((((((((('\n");
    fprintf(stdout, " `)))))))))))).-' \\___/ '-._(((((((((((\n");
    fprintf(stdout, "  `))))_._.-' __)(     )(_  '-._._(((('\n");
    fprintf(stdout, "   `))'---)___)))'\\_ _/'((((__(---'(('\n");
    fprintf(stdout, "     `))))))))))))|' '|(((((((((((('\n");
    fprintf(stdout, "      `)))))))))/'   '\\((((((((('\n");
    fprintf(stdout, "         `)))))))|     |((((((('\n");
    fprintf(stdout, "          `))))))|     |(((((('\n");
    fprintf(stdout, "                /'     '\\\n");
    fprintf(stdout, "               /'       '\\\n");
    fprintf(stdout, "              /'         '\\\n");
    fprintf(stdout, "             /'           '\\\n");
    fprintf(stdout, "             '---..___..---'\\\n");
  return 0;
}

int devil() {
    fprintf(stdout, "        _.---**""**-.\n");
    fprintf(stdout, "._   .-'           /|`.\n");
    fprintf(stdout, " \\`.'             / |  `.\n");
    fprintf(stdout, "  V              (  ;    \\\n");
    fprintf(stdout, "  L       _.-  -. `'      \\\n");
    fprintf(stdout, " / `-. _.'       \\         ;\n");
    fprintf(stdout, ":            __   ;    _   |\n");
    fprintf(stdout, ":`-.___.+-*\"': `  ;  .' `. |\n");
    fprintf(stdout, " |`-/     `--*'   /  /  /`.\\|\n");
    fprintf(stdout, ": :              \\    :`.| ;\n");
    fprintf(stdout, "| |   .           ;/ .' ' /\n");
    fprintf(stdout, ": :  / `             :__.'\n");
    fprintf(stdout, " \\`._.-'       /     |\n");
    fprintf(stdout, "  : )         :      ;\n");
    fprintf(stdout, "  :----.._    |     /\n");
    fprintf(stdout, " : .-.    `.       /\n");
    fprintf(stdout, "  \\     `._       /\n");
    fprintf(stdout, "  /`-            /\n");
    fprintf(stdout, " :             .'\n");
    fprintf(stdout, "  \\ )       .-'\n"); 
    fprintf(stdout, "   `-----*\"'\n");
  return 0;
}