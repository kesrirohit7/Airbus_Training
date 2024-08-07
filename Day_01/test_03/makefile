CC = gcc
CCFLAG1 = -Wno-implicit-function-declaration -c
EXEC = final
OBJS = first.o second.o third.o fourth.o

%.o:%.c
	@echo Compiling $<
	$(CC) $(CCFLAG1) $< -o $@
	@echo $@ Compiled

$(EXEC):$(OBJS)
	$(CC) $(OBJS) -o $(EXEC)

clean:
	rm *.o final
