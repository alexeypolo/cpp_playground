#include <iostream>
#include <string>
#include <functional>

struct pair_t {
    int val;
    int (*func)(const std::string&);
};

int main(void)
{
    //std::function<int (const std::string&)> func =
    auto func =
        [](const std::string& str) { std::cout << "A: " << str << std::endl; };

    pair_t pairs[] = {
        { 0, [](const std::string& str) ->int { std::cout << "A: " << str << std::endl; return 0; } },
        { 0, [](const std::string& str) ->int { std::cout << "B: " << str << std::endl; return 0; } },
        { 0, [](const std::string& str) ->int { std::cout << "C: " << str << std::endl; return 0; } },
        { 0, [](const std::string& str) ->int { std::cout << "D: " << str << std::endl; return 0; } }
    };

    for (int i=0; i < sizeof(pairs)/sizeof(pairs[0]); i++) {
        pairs[i].func("hello");
    }

    return 0;
}
