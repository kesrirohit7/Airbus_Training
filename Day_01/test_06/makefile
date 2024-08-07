CC = gcc
CCFLAG1 = -Wno-implicit-function-declaration -c
EXEC = final

SRCDIR = src
OBJDIR = target
LIBDIR = bin/dist

SRCS = $(wildcard $(SRCDIR)/*.c)
OBJS = $(SRCS:$(SRCDIR)/%.c=$(OBJDIR)/%.o)

$(OBJDIR)/%.o:$(SRCDIR)/%.c
	@echo "Compiling $<"
	$(CC) $(CCFLAG1) $< -o $@
	@echo "$@ Compiled"

$(EXEC):$(OBJS)
	$(CC) $^ -o $(LIBDIR)/$(EXEC)

clean:
	rm -f $(OBJDIR)/*.o $(LIBDIR)/$(EXEC)
