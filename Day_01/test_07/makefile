# Compiler to use
CC = gcc

# Compiler flags, including warning suppression for implicit function declarations
CCFLAGS = -Wno-implicit-function-declaration

# Name of the final executable
EXEC = final

# Source, object, and library directories
SRCDIR = src
OBJDIR = target
LIBDIR = bin/dist

# Get all .c files in the source directory
SRCS = $(wildcard $(SRCDIR)/*.c)


# Replace .c file extensions with .o in the object directory
OBJS = $(SRCS:$(SRCDIR)/%.c=$(OBJDIR)/%.o)

# Create object directory if it does not exist
$(OBJDIR):
	mkdir -p $(OBJDIR)

# Create library directory if it does not exist
$(LIBDIR):
	mkdir -p $(LIBDIR)

# Rule for building object files
$(OBJDIR)/%.o:$(SRCDIR)/%.c | $(OBJDIR)
	@echo "Compiling $<"
	$(CC) $(CCFLAGS) -c $< -o $@
	@echo "$@ Compiled"
	@echo ""

# Rule for linking object files into the final executables
$(EXEC):$(OBJS) | $(LIBDIR)
	$(CC) $^ -o $(LIBDIR)/$(EXEC)

# Clean up build artifacts
.PHONY: clean
clean:
	rm -f $(OBJDIR)/*.o $(LIBDIR)/$(EXEC)
