SRC=$(wildcard *cpp)
BIN=$(patsubst %.cpp,%,$(SRC))
OBJ=$(patsubst %.cpp,%.o,$(SRC))

all: $(BIN)
	@echo OK

clean:
	rm -f $(BIN)

%: %.cpp
	g++ -std=c++14 $< -o $@
