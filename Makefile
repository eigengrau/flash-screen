CFLAGS  = `pkg-config --cflags gtk+-3.0 libcanberra-gtk3`
LDFLAGS = `pkg-config --libs   gtk+-3.0 libcanberra-gtk3`
PREFIX  = usr/local

all: build

build: cheese-flash.o sound.o main.o
	$(CC) $(CFLAGS) $(LDFLAGS) $+ -o flash-screen

%.o: %.c
	$(CC) $(CFLAGS) -c $<

.PHONY: clean
clean:
	rm -f *.o
	rm -f flash-screen

install: build
	install -Dm755 flash-screen $(DESTDIR)/$(PREFIX)/bin/flash-screen
