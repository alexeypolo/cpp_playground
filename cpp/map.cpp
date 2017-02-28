#include <iostream>
#include <map>
#include <string>

struct Entry {
  int x;
  std::string str;
  Entry(int x, std::string str) : x(x), str(str) { std::cout << __func__ << ":" << x << "," << str << "\n"; }
};

int main ()
{
  std::map<char,Entry> mymap;

  {
    auto res_pair = mymap.emplace('x', Entry(1, "foo"));
    std::cout << "emplace returns:" << res_pair.second << "\n";
  } {
    auto res_pair = mymap.emplace('y', Entry(2, "bar"));
    std::cout << "emplace returns:" << res_pair.second << "\n";
  } {
    auto res_pair = mymap.emplace('x', Entry(0xBAD, "bad"));
    std::cout << "emplace returns:" << res_pair.second << "\n";
  }

  std::cout << "mymap contains:";
  for (auto& x: mymap)
    std::cout << " [" << x.first << ':' << x.second.str << ']';
  std::cout << '\n';

  return 0;
}

