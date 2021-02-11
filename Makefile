.PHONY: install run

BIN = docker run \
			--interactive \
			--rm \
			-v "/code" \
			--name reversi-python-running \
			reversi-python

# Initialisation ===============================================================

install:
	docker build --tag=reversi-python .

# Executer ===============================================================

run:
	 $(BIN) ./src/reversi.py
