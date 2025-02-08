TARGET = main
CC = gcc
CFLAGS = -Wall -Wextra -std=c11
all: $(TARGET)
$(TARGET): main.o
	$(CC) $(CFLAGS) -o $(TARGET) main.o
main.o: main.c
	$(CC) $(CFLAGS) -c main.c
clean:
	rm -f $(TARGET) main.o