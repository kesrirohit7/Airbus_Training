first.o:first.c
	gcc -Wno-implicit-function-declaration -c first.c -o first.o

second.o:second.c
	gcc -Wno-implicit-function-declaration -c second.c -o second.o

third.o:third.c
	gcc -Wno-implicit-function-declaration -c third.c -o third.o

fourth.o:fourth.c
	gcc -Wno-implicit-function-declaration -c fourth.c -o fourth.o

final:first.o second.o third.o fourth.o
	gcc first.o second.o third.o fourth.o -o final

clean:
	rm first.o second.o third.o fourth.o final
