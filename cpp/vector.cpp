#include <iostream>
#include <vector>
#include <algorithm>    // std::rotate

struct Foo {
    int val;
    Foo() : val(0) {}
    Foo(int val) : val(val) { std::cout << "Foo(" << val << ")\n"; }
};

void vector_dump(std::vector<Foo> &vector, const char *msg) {
  std::vector<Foo>::iterator it;

  std::cout << msg << "\n";
  for (it=vector.begin(); it<vector.end(); it++)
    std::cout << ' ' << it->val;
  std::cout << '\n';
}

int main ()
{
  std::vector<const char*> bar({"a", "b", "c"});
  std::vector<Foo> vec(10);
  std::vector<Foo>::iterator it;
  int i;

  for (i=0, it=vec.begin(); it<vec.end(); it++, i++)
    *it = Foo(i);

  vector_dump(vec, "initial");

  std::rotate(vec.begin(), vec.end()-1, vec.end());
  vector_dump(vec, "after rotate");

  return 0;
}

