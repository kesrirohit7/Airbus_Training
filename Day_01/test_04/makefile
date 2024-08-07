CC = gcc
CCFLAG1 = -Wno-implicit-function-declaration -c
EXEC = final
SRCS = $(wildcard *.c)
OBJS = $(SRCS:.c=.o)

%.o:%.c
	@echo Compiling $<
	$(CC) $(CCFLAG1) $< -o $@
	@echo $@ Compiled

$(EXEC):$(OBJS)
	$(CC) $(OBJS) -o $(EXEC)

clean:
	rm -f *.o $(EXEC)
