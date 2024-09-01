# Makefile

# Variáveis
CC = clang
CFLAGS = -Wall -Wextra -O2
TARGET = interpreter
SRC = main.c
PYTHON_SCRIPT = parser.py
JS_SCRIPT = interpreter.js
PSR_FILE = mp.psr
BIB_CREATE_SCRIPT = create_bib.py

# Regras
all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)

run: $(TARGET)
	./$(TARGET)

run_python: $(PYTHON_SCRIPT)
	python3 $(PYTHON_SCRIPT)

run_js: $(JS_SCRIPT)
	node $(JS_SCRIPT)

test: $(TARGET) $(PSR_FILE)
	./$(TARGET) $(PSR_FILE)

clean:
	rm -f $(TARGET)

# Regras adicionais
run_interpreter:
	./$(TARGET) $(PSR_FILE)

run_all: run_python run_js

install: $(TARGET)
	cp $(TARGET) /usr/local/bin/

create_bib:
	python3 $(BIB_CREATE_SCRIPT)

# Adicione mais regras conforme necessário
