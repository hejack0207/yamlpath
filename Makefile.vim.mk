diag:
	@echo $(.SHELLFLAGS)
	# verify if python3 works
	vim --version | grep +python3 || echo "current vim NOT support python3"
	vim -es --not-a-term -S tools.vim -c 'call Pyinfo()' -c q
	# verify if vim bridge works
	python3 -m pip list | grep vim-bridge || python3 -m pip install vim-bridge
	vim -es --not-a-term -S tools.vim -c 'call VerifyBridge()' -c q

.ONESHELL:
ifeq ($(SHELL),/bin/sh)
.SHELLFLAGS = -ce
endif
