CC = gcc
CCFLAG1 = -Wno-implicit-function-declaration -c

OBJS = first.o second.o third.o fourth.o

first.o:first.c
	@echo Compiling first.c
	$(CC) $(CCFLAG1) first.c -o first.o
	@echo first.o Compiled

second.o:second.c
	@echo Compiling second.c
	$(CC) $(CCFLAG1) second.c -o second.o
	@echo second.o Compiled

third.o:third.c
	@echo Compiling third.c
	$(CC) $(CCFLAG1) third.c -o third.o
	@echo third.o Compiled

fourth.o:fourth.c
	@echo Compiling fourth.c
	$(CC) $(CCFLAG1) fourth.c -o fourth.o
	@echo fourth.o Compiled

final:$(OBJS)
	$(CC) $(OBJS) -o final

clean:
	rm *.o final
