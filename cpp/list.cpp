// splicing lists
#include <iostream>
#include <list>

struct Data {
  Data(int val) : val(val) { std::cout << "Data(" << val << ")\n"; }
  int val;
};

void list_dump(std::list<Data> &list, const char *msg) {
  std::list<Data>::iterator it;

  std::cout << msg;
  for (it=list.begin(); it!=list.end(); ++it)
    std::cout << ' ' << it->val;
  std::cout << '\n';
}

void list_populate(std::list<Data> &list, int min, int max) {
  for (int i=min; i<=max; ++i)
     list.push_back(Data(i));
}

int main ()
{
  std::list<Data> mylist1, mylist2;
  std::list<Data>::iterator it;

  // set some initial values:
  list_populate(mylist1, 1, 4);     // mylist1: 1 2 3 4
  list_populate(mylist2, 10, 13);     // mylist1: 10 11 12 13

  it = mylist1.begin();
  ++it;                         // points to 2

  mylist1.splice (it, mylist2); // mylist1: 1 10 20 30 2 3 4
                                // mylist2 (empty)
                                // "it" still points to 2 (the 5th element)

  mylist2.splice (mylist2.begin(),mylist1, it);
                                // mylist1: 1 10 20 30 3 4
                                // mylist2: 2
                                // "it" is now invalid.
  it = mylist1.begin();
  std::advance(it,3);           // "it" points now to 30

  mylist1.splice ( mylist1.begin(), mylist1, it, mylist1.end());
                                // mylist1: 30 3 4 1 10 20

  list_dump(mylist1, "mylist1 contains:");
  list_dump(mylist2, "mylist2 contains:");

  // rotate mylist1
  Data &element = mylist1.back();
  mylist1.pop_back();
  mylist1.push_front(element);
  list_dump(mylist1, "rotated mylist1 contains:");
  element.val = 17;
  list_dump(mylist1, "17 assigned through reference:");

  // 3rd element in mylist1
  it = mylist1.begin();
  std::advance(it, 3);
  std::cout << "mylist1[3] = " << it->val << "\n";

  return 0;
}

