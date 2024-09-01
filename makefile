# Makefile

# Variáveis
CC = clang
CFLAGS = -Wall -Wextra -O2
TARGET = interpreter
SRC = main.c
PYTHON_SCRIPT = parser.py
JS_SCRIPT = interpreter.js
PSR_FILE = mp.psr

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

# Adiciona regras adicionais conforme necessário

# Exemplo de regra para executar o interpretador com um arquivo PSR
run_interpreter:
	./$(TARGET) $(PSR_FILE)

# Regra para executar scripts Python e JavaScript
run_all: run_python run_js

# Regra para instalar o binário no diretório de binários do sistema
install: $(TARGET)
	cp $(TARGET) /usr/local/bin/

# Adicione mais regras conforme necessário
