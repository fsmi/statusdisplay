/*
This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar and 
reproduced below.

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
Version 2, December 2004 

Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 

	Everyone is permitted to copy and distribute verbatim or modified 
	copies of this license document, and changing it is allowed as long 
	as the name is changed. 

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

	0. You just DO WHAT THE FUCK YOU WANT TO.
*/

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <linux/input.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char** argv){
	int fd;
	char name[512];

	if(argc != 2){
		fprintf(stderr, "evname - Print evdev name for a device node\n");
		fprintf(stderr, "Use as:\n");
		fprintf(stderr, "\t%s <node>", argv[0]);
		return EXIT_FAILURE;
	}

	fd = open(argv[1], O_RDONLY);
	if(fd < 0){
		perror("open");
		return EXIT_FAILURE;
	}

	if(ioctl(fd, EVIOCGNAME(sizeof(name)), name) < 0){
		perror("ioctl");
		close(fd);
		return EXIT_FAILURE;
	}

	puts(name);
	close(fd);
	return 0;
}
