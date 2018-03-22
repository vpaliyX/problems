#include "lru.hpp"

int main(int argc, char** argv) {
  lru<int,int> cache(10);
  cache.put(1,2);
  std::cout<<cache.get(1)<<std::endl;
  return 1;
}
