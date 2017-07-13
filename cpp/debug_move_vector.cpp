#include <stdio.h>
#include <vector>
#include <cassert>

// debug vector
template <class T>
class dvector : public std::vector<T> {
public:
    dvector() : std::vector<T>() {
        printf("** default c'tor\n");
    }
    dvector(size_t sz) : std::vector<T>(sz) {
        printf("** size c'tor\n");
    }
    dvector(const dvector& other) : std::vector<T>(other) {
        printf("** copy c'tor\n");
    }
    dvector(dvector&& other) : std::vector<T>(std::move(other)) {
        printf("** move c'tor\n");
    }
    dvector& operator=(const dvector& other) {
        printf("** copy assignment\n");
        std::vector<T>::operator=(other);
        return *this;
    }
    dvector& operator=(const dvector&& other) {
        printf("** move assignment\n");
        std::vector<T>::operator=(std::move(other));
        return *this;
    }
};

void write_reg_rvalue(int addr, dvector<uint8_t>&& v) {
    printf("** %s: v.size() %ld\n", __func__, v.size());
}

void write_reg(int addr, dvector<uint8_t> v) {
    printf("** %s: v.size() %ld\n", __func__, v.size());
}

int main(void) {
    dvector<uint8_t> v(5), v2, v3;

    for (int i=0; i < 5; i++) { v[i] = i; }

    printf("before assignment: v {%ld,%p}, v2 {%ld,%p}, v3 {%ld,%p}\n", v.size(), v.data(), v2.size(), v2.data(), v3.size(), v3.data());

    v2 = v; v3 = v;

    printf("after assignment: v {%ld,%p}, v2 {%ld,%p}, v3 {%ld,%p}\n", v.size(), v.data(), v2.size(), v2.data(), v3.size(), v3.data());

    printf("call write_reg_rvalue\n");
    write_reg_rvalue(17, std::move(v));

    printf("call write_reg w/ move\n");
    write_reg(17, std::move(v2));

    printf("call write_reg w/o move\n");
    write_reg(17, v3);

    printf("after write_reg_XXX: v {%ld,%p}, v2 {%ld,%p}, v3 {%ld,%p}\n", v.size(), v.data(), v2.size(), v2.data(), v3.size(), v3.data());

    assert(!v.empty());
    assert(v2.empty()); // only v2 was moved!
    assert(!v3.empty());

    return 0;
}
