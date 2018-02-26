.PHONY: all

MKDIR ?= mkdir -p

all:
	$(MAKE) -C inputtools
	$(MAKE) -C martrix
	$(MAKE) -C mpdinfo
	$(MAKE) -C rpcd
	$(MAKE) -C timers-cli
	$(MAKE) -C xecho
	$(MAKE) -C xelflut
	$(MKDIR) dolphin/Build
	cd dolphin/Build && cmake ..
	$(MAKE) -C dolphin/Build
	$(MAKE) evname
