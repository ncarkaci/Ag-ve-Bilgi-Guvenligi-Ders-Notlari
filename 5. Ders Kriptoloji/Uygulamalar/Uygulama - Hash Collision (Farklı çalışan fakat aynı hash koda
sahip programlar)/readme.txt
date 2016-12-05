Quick usage instructions:

Note for Windows users: the below instructions are for Unix/Linux. On Windows, you may have to append ".exe" to the names of executable files. Also, to use "make", you must have the GNU tools installed and working.

Unpack the archive and build the library and tools:
    tar zxf evilize-0.2.tar.gz
    cd evilize-0.2
    make
This creates the programs "evilize", "md5coll", and the object file "goodevil.o".
Create a C program with multiple behaviors. Instead of the usual top-level function main(), write two separate top-level functions main_good() and main_evil(). See the file hello-erase.c for a simple example.
Compile your program and link against goodevil.o. For example:
    gcc hello-erase.c goodevil.o -o hello-erase
Run the following command to create an initialization vector:
    ./evilize hello-erase -i
Create an MD5 collision by running the following command (but replace the vector on the command line with the one you found in step 4):
    ./md5coll 0x23d3e487 0x3e3ea619 0xc7bdd6fa 0x2d0271e7 > init.txt
Note: this step can take several hours.
Create a pair of good and evil programs by running:
    ./evilize hello-erase -c init.txt -g good -e evil
Here "good" and "evil" are the names of the two programs generated, and "hello-erase" is the name of the program you created in step 3.
NOTE: steps 4-6 can also be done in a single step, as follows:

    ./evilize hello-erase -g good -e evil
However, I prefer to do the steps separately, since step 5 takes so long.
Check the MD5 checksums of the files "good" and "evil"; they should be the same.
Run the programs "good" and "evil" - they should exhibit the two different behaviors that you programmed in step 2.